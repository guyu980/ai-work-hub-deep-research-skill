# AI Work Hub Deep Research

[English](README.md)

**正式行业与技术研究**。在明确需要深度研究或系统报告时，用易懂的语言和图示讲清技术原理，从证据形成行业趋势与价值归属判断，交付图文结合的 Markdown 与可浏览的 HTML。普通访谈和外部查证不自动升级为正式研究。

## 安装与更新

也可以直接让 Codex 从此 GitHub 仓库安装 Skill，并先检查是否已有安装。推荐 Git 克隆加单个软链接，让自用版和分享版使用同一源码：

```bash
mkdir -p ~/Documents/skills-repos ~/.codex/skills
cd ~/Documents/skills-repos
git clone https://github.com/guyu980/ai-work-hub-deep-research-skill.git
ln -s "$(pwd)/ai-work-hub-deep-research-skill/ai-work-hub-deep-research" ~/.codex/skills/ai-work-hub-deep-research
```

已有同名目录时先检查，不覆盖安装，避免出现重复 Skill。Python 脚本需要 Python 3.10+；Graph 共享锁支持 macOS/Linux。安装后重新加载 Codex。更新时：

```bash
cd ~/Documents/skills-repos/ai-work-hub-deep-research-skill
git pull --ff-only
```

软链接立即使用同一份代码，无需复制另一份 Skill。私人工作区与仓库分开。

## 日常使用

```text
用 $ai-work-hub-deep-research 研究这个技术方向，重点解释路线取舍、客户价值和投资机会。
基于项目材料做独立行业研究，说明哪些假设支持或反对当前判断。
仅在对话中研究，不生成文件。
```

先复用已有判断、研究及专家来源，再围绕问题开展分析。机制、竞争、市场模型、技术趋势与估值是可选模块，不机械要求每份报告都有五年预测或完整市场审计。重要研究可充分展开；不重复逐条证据记账，也不默认要求工程复现。

明确要求深度研究时，按专业研究标准投入：拆解问题层次，实读重要原始资料，核对关键数据和冲突解释，建立必要的独立测算。条件允许时采用专业分工和独立反方审阅，由主审统一综合。重要推理薄弱处须补查、重算并改写；不为节省工作量或 token 削减必要分析。完成依据是实质覆盖和结论质量，不以篇幅、引用数量或声称投入的人月衡量。

原理从具体任务或小例子讲起，先解释过程、作用与代价，再引入必要术语。趋势研究比较竞争解释，推导约束变化怎样影响客户采购、竞争与利润，并说明当前更倾向哪种判断。仅列成功与失败情景还不足以完成研究。

在构思正文时主动设计机制示意、结构剖面、步骤演示、前后对照、瓶颈迁移、价值流与条件情景图。参数变化、时间过程或空间关系适合动态理解时，可使用交互控件、动画与 3D，同时保留可打印、可分享的静态视图。图的形式和数量随解释需要选择。参见[虚构图文示例](ai-work-hub-deep-research/examples/receipt-workflow.md)。

项目相关报告放在 `输出文档/03_研究与分析/`，独立报告放在 `行业研究/<主题>/`。初始化只创建需要的报告与状态；研究所需图示和模型在写作中生成。默认 HTML 沿用简洁的斯坦福红视觉系统，交互演示作为本地配套内容与正式报告互相链接。

每份报告是有明确信息截至日的研究快照。日后普通新闻更新现行 Graph 或项目判断，不自动重做所有历史报告；重大或明确要求的修订再更新 Markdown 和 HTML。旧研究若回答不同问题仍保留。

交付前审读读者能否讲清原理、结论是否经过因果推导、反方是否真正影响取舍，并检查实际图示和互动效果。自动校验负责结构和计算约束，不能替代内容质量与可读性审阅。

```bash
python3 ai-work-hub-deep-research/scripts/render_report.py --input "<报告.md>" --output "<报告.html>" --title "<标题>"
python3 ai-work-hub-deep-research/scripts/validate_research.py --report "<报告.md>" --html "<报告.html>"
```

## 三个 Skill 如何衔接

[尽调](https://github.com/guyu980/ai-work-hub-diligence-skill)维护单公司现行判断；[Memory Graph](https://github.com/guyu980/ai-work-hub-memory-graph-skill)整理非项目来源和跨项目记忆；[深度研究](https://github.com/guyu980/ai-work-hub-deep-research-skill)负责明确要求的正式报告。安装同伴 Skill 可以联动，也可单独使用。新闻与 GitHub 发现由已授权的自动化任务执行，Skill 本身不自动创建定时任务。

公开仓库只保存通用机制、脚本和虚拟案例。实际项目、知识库、报告、私人关注名单、交付地址和凭据保留本地，不上传。贡献通过 PR，由维护者审阅合并。模型选择属于运行设置，Skill 不绑定某个模型。

[Agent 执行入口](ai-work-hub-deep-research/SKILL.md) · [MIT](LICENSE)
