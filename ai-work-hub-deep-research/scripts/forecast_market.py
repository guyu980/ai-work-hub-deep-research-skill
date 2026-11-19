#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path
from stat import S_IMODE
from tempfile import TemporaryDirectory


REQUIRED = [
    "scenario", "geography", "segment", "year", "currency",
    "addressable_units", "paid_penetration", "hardware_bom",
    "software_service_ratio", "fx_to_cny", "units_source",
    "penetration_source", "price_source",
]
CALCULATED = ["paid_units", "hardware_revenue", "software_service_revenue", "total_revenue", "total_revenue_cny", "row_type"]


def decimal_value(row: dict[str, str], key: str, row_number: int) -> Decimal:
    try:
        value = Decimal(row[key].replace(",", "").strip())
        if not value.is_finite():
            raise InvalidOperation
        return value
    except (InvalidOperation, AttributeError) as exc:
        raise ValueError(f"row {row_number}: invalid decimal in {key}: {row.get(key)!r}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate a transparent shipment/BOM market forecast.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.input.resolve() == args.output.resolve():
        raise SystemExit("choose a separate output to preserve the model inputs")
    with args.input.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        if any(not key for key in headers) or len(set(headers)) != len(headers):
            raise SystemExit("input has empty or duplicate column names")
        if set(headers).intersection(CALCULATED):
            raise SystemExit("input contains calculated output columns; use the driver file")
        missing = [column for column in REQUIRED if column not in headers]
        if missing:
            raise SystemExit(f"missing columns: {', '.join(missing)}")
        rows = list(reader)
    if not rows:
        raise SystemExit("market model has no data rows")

    details: list[dict[str, str]] = []
    totals: dict[tuple[str, str, str, str], dict[str, Decimal]] = {}
    for row_number, row in enumerate(rows, 2):
        if None in row or None in row.values():
            raise SystemExit(f"row {row_number}: row width differs from the header")
        units = decimal_value(row, "addressable_units", row_number)
        penetration = decimal_value(row, "paid_penetration", row_number)
        bom = decimal_value(row, "hardware_bom", row_number)
        service_ratio = decimal_value(row, "software_service_ratio", row_number)
        fx = decimal_value(row, "fx_to_cny", row_number)
        if units < 0 or bom < 0 or service_ratio < 0 or fx <= 0:
            raise SystemExit(f"row {row_number}: units/BOM/service ratio must be non-negative and FX positive")
        if not Decimal("0") <= penetration <= Decimal("1"):
            raise SystemExit(f"row {row_number}: paid_penetration must be between 0 and 1")
        try:
            int(row["year"])
        except ValueError as exc:
            raise SystemExit(f"row {row_number}: year must be an integer") from exc

        paid_units = units * penetration
        hardware_revenue = paid_units * bom
        service_revenue = hardware_revenue * service_ratio
        total_revenue = hardware_revenue + service_revenue
        total_cny = total_revenue * fx
        result = dict(row)
        result.update(
            {
                "paid_units": f"{paid_units:.4f}",
                "hardware_revenue": f"{hardware_revenue:.4f}",
                "software_service_revenue": f"{service_revenue:.4f}",
                "total_revenue": f"{total_revenue:.4f}",
                "total_revenue_cny": f"{total_cny:.4f}",
                "row_type": "detail",
            }
        )
        details.append(result)
        key = (row["scenario"], row["geography"], row["year"], row["currency"])
        bucket = totals.setdefault(
            key,
            {"paid_units": Decimal(0), "hardware": Decimal(0), "service": Decimal(0), "total": Decimal(0), "cny": Decimal(0)},
        )
        bucket["paid_units"] += paid_units
        bucket["hardware"] += hardware_revenue
        bucket["service"] += service_revenue
        bucket["total"] += total_revenue
        bucket["cny"] += total_cny

    output_fields = REQUIRED + [key for key in headers if key not in REQUIRED] + CALCULATED
    total_rows: list[dict[str, str]] = []
    for (scenario, geography, year, currency), values in sorted(totals.items()):
        total_rows.append(
            {
                "scenario": scenario, "geography": geography, "segment": "TOTAL",
                "year": year, "currency": currency, "addressable_units": "",
                "paid_penetration": "", "hardware_bom": "",
                "software_service_ratio": "", "fx_to_cny": "",
                "units_source": "aggregated detail rows", "penetration_source": "",
                "price_source": "", "paid_units": f"{values['paid_units']:.4f}",
                "hardware_revenue": f"{values['hardware']:.4f}",
                "software_service_revenue": f"{values['service']:.4f}",
                "total_revenue": f"{values['total']:.4f}",
                "total_revenue_cny": f"{values['cny']:.4f}", "row_type": "total",
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix=".forecast-", dir=args.output.parent) as directory:
        temporary = Path(directory) / "forecast.csv"
        with temporary.open("x", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=output_fields)
            writer.writeheader()
            writer.writerows(details)
            writer.writerows(total_rows)
        if args.output.exists():
            temporary.chmod(S_IMODE(args.output.stat().st_mode))
        temporary.replace(args.output)
    print(args.output)
    print(f"detail rows: {len(details)}")
    print(f"total rows: {len(total_rows)}")


if __name__ == "__main__":
    main()
