# Technology And Competition Analysis

## Contents

1. Explain the mechanism in ordinary language
2. Compare routes through customer tasks
3. Technology development and moving bottlenecks
4. Competition and company advantage

## Explain The Mechanism In Ordinary Language

The reader should be able to explain what happens, why it helps and what it costs without already knowing the technical vocabulary. A list of components, a glossary or an acronym-heavy diagram does not achieve this.

For a consequential mechanism, develop a connected explanation:

- **Start with one concrete task.** Describe the input, desired result and operating conditions. Keep a small example running through the explanation so the reader can follow the same object, signal, data item or piece of work.
- **Show the existing approach and its constraint.** What is waiting, expensive, unreliable or impossible? Explain why simply using more of the old approach does not solve the problem economically.
- **Walk through the new mechanism.** Show what changes at each important step, including the step that creates the benefit. Name the technical concept after explaining its job; introduce only terms needed later in the argument.
- **Explain the trade-off and boundary.** Where does the gain come from, which resource pays for it, and when does it disappear? Separate what the mechanism can in principle do from demonstrated performance and commercial readiness.
- **Return to the task.** Translate the mechanism into a result the customer values: less waiting, fewer failures, more throughput, lower operating cost or a previously unavailable capability.

Depth follows the research question. Fully develop the mechanisms behind the central judgment; summarize peripheral technologies. Do not compress a requested deep explanation into a paragraph of definitions.

For the core routes in a deep study, go beyond a helpful analogy to the variables that govern performance and cost. Explain the relevant scaling relationship, resource limit or failure mechanism, using a calculation or derivation where it clarifies the choice. Reconstruct why earlier routes reached their limits and what the new approach changes in those limits. Compare decisive literature and product evidence on equivalent conditions, including negative results or implementation constraints. Plain language is the way to expose this depth, not a reason to omit it.

Choose an explanation path that fits the technology rather than imposing a sensing chain on every domain:

| Domain | Useful objects to follow | Questions that expose the mechanism |
| --- | --- | --- |
| Physical systems, materials and sensing | Force, energy, matter or signal through the relevant structure | What physically changes? What is measured directly and what is inferred? Where do loss, noise, drift or failure enter? |
| Compute, chips, algorithms and models | One request, instruction, data item or training example | Where is information stored and moved? Which operations happen, wait or run together? What changes in compute, memory, communication, error or power? |
| Software, platforms and workflows | A user request and the handoffs needed to complete it | Who performs each step? What state or context is retained? What becomes automatic, and where do exceptions, permissions or integration work remain? |

A hybrid system may need more than one path. Use the relevant one at each level, and explain the connection between levels.

For example, before introducing a processor's out-of-order execution:

> A processor sometimes waits for data from memory. Some later calculations do not need that data, so they can run during the wait. The processor tracks which calculations depend on which results, does the available work early, and confirms the results in the order the program requires. This hides some waiting; it also needs more tracking hardware and power. If the later work depends on the missing data too, the benefit shrinks.

An analogy can help the reader enter the explanation, but return to the actual mechanism and say where the analogy breaks. Use equations when they clarify a dependency; define the quantities, give an intuitive example and state the conditions under which the relationship holds.

Draw the parts of the mechanism that are hard to understand from prose: a before/after process, a cross-section, a sequence of state changes, movement of data or the location of a bottleneck. Label arrows with what moves or changes. Explain what the figure establishes and its limits; see [html-and-visuals.md](html-and-visuals.md) for implementation and inspection.

## Compare Routes Through Customer Tasks

Define the task and system boundary before ranking routes. Compare credible alternatives, including improving the current approach, buying an integrated product, self-building or removing the need for the capability. Different tasks may favor different routes.

Choose the few dimensions that explain the choice, using the same basis across alternatives. Relevant dimensions may include:

- **Task performance:** success rate, accuracy, usable range, effective bandwidth, latency or throughput under relevant conditions.
- **Resources and system fit:** energy, memory, compute, data movement, physical space, interfaces, integration and human effort.
- **Reliability and operation:** drift, failure recovery, maintenance, calibration, security, replacement or exception handling.
- **Economics and adoption:** acquisition cost, engineering effort, qualification time, yield, service cost, switching cost and total cost per useful result.

Connect each decisive comparison to a customer consequence. A better component specification may have little value if a different part of the system determines the outcome. Sampling rate is not usable bandwidth; a benchmark score is not workflow success; lower unit cost is not necessarily lower cost per completed task. Check such distinctions where they affect the thesis, not as a universal audit list.

Where a comparison table helps, include both the advantage and the condition that makes it valuable. End with a reasoned preference by task, including why the strongest alternative does not win there. If evidence cannot distinguish the routes, explain the unresolved trade-off and its consequence instead of inventing a score.

## Technology Development And Moving Bottlenecks

Explain how progress changes the limiting factor. A faster model can make data movement dominant; cheaper components can make installation and maintenance dominate; easier integration can shift competition toward distribution. These are hypotheses to test in the subject at hand, not universal outcomes.

Trace the relevant dependencies from research result through engineering, cost and customer adoption. These stages can move at different speeds. For example, a reproducible laboratory gain may still depend on packaging or data access before it changes a product, and the product may still need a compelling replacement case before a customer switches.

Describe the current constraint, the development that could relax it, the constraint likely to bind next and who is positioned to solve that next problem. Compare the importance of further headline performance gains with progress in integration, reliability, cost or product design. Use the industry synthesis in [research-method.md](research-method.md) to derive effects on procurement and value capture.

Choose a horizon useful to the question. A dependency diagram or milestone sequence often explains timing better than an annual forecast table. Give calendar estimates only when the evidence supports them; distinguish announced plans from analyst estimates. Explain what must happen first, what can develop in parallel and what could delay or accelerate adoption. Avoid assigning a different theme to each year merely to fill a timeline.

## Competition And Company Advantage

Build the competitive landscape around the customer's alternatives and the sources of advantage. Include incumbents, specialists, startups, customer self-build, open source and architectural substitutes where they affect the answer; a logo wall or mandatory census of every category is insufficient.

For important players, establish the technical route, target task, product and commercial maturity, then explain the consequential differences in distribution, integration, data, manufacturing, economics or switching costs. Include ownership, financing and valuation evidence when relevant to the decision. Attribute company claims and distinguish observed deployments from plans without requiring an audit of every disclosed number.

Do not assume startups win emerging markets or incumbents win stable ones. Examine whether the changed bottleneck strengthens an existing advantage, makes it obsolete or creates a new one. In particular:

- Does customization create reusable capability and improve later deliveries, or does each new customer restart engineering work?
- Does standardization broaden the addressable market faster than it reduces differentiation and price?
- Does open source expand paid demand, reduce the scarcity of the product, or do both for different customer groups?
- Can an incumbent bundle the capability, or a customer internalize it, at an acceptable level of performance?
- Is the company gaining market share, benefiting from category growth, or temporarily receiving spending that will move to another layer?

Explain the likely basis of enduring profit and the strongest reason that judgment could fail. When supported, describe a consolidation path such as integration, acquisition, platform control or durable specialization. Industry adoption alone does not establish a viable independent company or an attractive investment at the proposed price.
