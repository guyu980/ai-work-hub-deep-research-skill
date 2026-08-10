# AI Work Hub Deep Research

[English](README.md)

面向投资决策的 Codex 深度研究 Skill。既可以从一个在研项目切入，也可以直接研究一个行业、技术主题、产业链或跨项目专题。

## 能做什么

- 重建系统边界、底层技术原理和完整信号链。
- 用同一套工程与商业指标比较技术路线、替代方案和“不使用专用产品”的架构。
- 分别判断未来五年的论文前沿、工程瓶颈、制造成本、接口标准、产品形态和商业采用趋势。
- 梳理全球与中国竞争格局，同时覆盖传统厂商、成熟专业公司、创业公司、OEM 自研和开源/学术生态。
- 建立全球与中国未来五年自下而上市场模型，包含保守、基准、乐观情景及敏感性分析。
- 输出投资判断、估值含义、证明门槛、反方观点和可能推翻结论的证据。
- 生成带 SVG 图示、响应式目录、窄屏适配和本地相对链接的 HTML 阅读版。
- 在安装配套 Skill 时，与私有 AI Work Hub Memory Graph 联动。

权威论文、标准、行业组织和可靠三方报告是证据输入，不是结论代理。流程会区分事实、来源观点、外部预测和本报告假设，再独立重建判断。

## 安装

```bash
mkdir -p ~/Documents/skills-repos ~/.codex/skills
cd ~/Documents/skills-repos
git clone https://github.com/guyu980/ai-work-hub-deep-research-skill.git
ln -s "$(pwd)/ai-work-hub-deep-research-skill/ai-work-hub-deep-research" \
  ~/.codex/skills/ai-work-hub-deep-research
```

如果目标路径已经存在，先检查后再处理。安装后如未立即显示，可重新加载 Codex。

## 使用示例

```text
使用 $ai-work-hub-deep-research 深入研究机器人触觉传感：讲清底层原理和不同路线，分析全球与中国竞格、未来五年技术趋势及市场规模，画出关键图示，并给出投资判断。
```

项目关联模式：

```text
使用 $ai-work-hub-deep-research 研究这个项目所在行业。先读项目资料，再独立重建行业逻辑，并说明公司必须证明什么。
```

## 与其他 Skill 的分工

- `ai-work-hub-diligence`：维护公司项目的一份持续判断、项目状态和后续尽调。
- `ai-work-hub-deep-research`：完成技术、产业、市场、竞争和投资专题的深度研究。
- `ai-work-hub-memory-graph`：检索和沉淀稀疏、可复用的项目、赛道、技术、估值、事件和人物知识。

行业报告是独立交付物；如果报告改变项目判断，应在报告完成后通过 diligence 工作流更新原有项目判断，而不是新增第二份判断。

## 公私边界

本公开仓库只包含通用指令、脚本、参考方法和模板。不得提交真实 BP、访谈原文、客户信息、项目判断、凭据、含私有数据的模型或生成后的 Memory Graph 内容。

许可证：[MIT](LICENSE)
