# job-hunt-skill

[English](README.md) · **简体中文**

一个把求职全流程跑完的 agent skill：对着真实 JD 做差距分析、背景提升与刷题计划、
简历定制、多平台找岗、以及带状态追踪的投递流水线。

适用于 Claude Code（自动加载 skill）、Codex CLI，以及任何能读文件、跑 Python 的
agent（它们读 `AGENTS.md`）。

## 安装

**项目级** —— clone 到任意位置，在里面工作：

```bash
git clone https://github.com/Chanpanship/job-hunt-skill.git && cd job-hunt-skill
```

**全局** —— 任何目录、任何会话都能用：

```bash
git clone https://github.com/Chanpanship/job-hunt-skill.git /tmp/jhs && cp -r /tmp/jhs/.claude/skills/job-hunt ~/.claude/skills/
```

skill 的发现路径是「当前工作目录下的 `.claude/skills/`」或 `~/.claude/skills/`。
在 Claude Code 里，你提到找工作相关的事情它会自动加载；其他 agent 需要你让它先读
`AGENTS.md`。

依赖：Python 3（仅标准库，无第三方依赖）。

## 开始用

把 agent 指向这个文件夹，然后用大白话跟它说：

> 帮我找工作，我的简历在 `<路径>`

**Claude Code（桌面 App）**——把这个文件夹作为项目打开。你提到找工作相关的事情时 skill 自动加载，无需执行任何命令。

**Claude Code（终端）**——在本目录下运行 `claude`。

**Codex CLI / Codex 桌面 App**——把项目目录作为工作区打开，并让它先读
`AGENTS.md`；Codex 会按其中说明加载 `.codex/skills/job-hunt/SKILL.md`。

如果你明确要求填申请表，Codex 可以用 Computer Use 操作现有浏览器窗口：打开岗位、
上传定制简历、填写普通字段、起草筛选题答案，并在最终 Submit / Apply / Send 前停下，
交回给你检查和点击。它不会登录、创建账号、处理凭据、绕过 CAPTCHA，也不会替你回答
工作许可/签证、犯罪记录、既往任职和自我身份识别等法律声明题。

之后就是正常对话：「帮我找新加坡的岗位」「这个岗位帮我改一版简历」「我这周投得怎么样」。
状态存在 `workspace/`，所以下次开会话是接着走，而不是重新问你一遍。

skill 自带的两个 Python 脚本是 agent 调用的，不需要你动手。
## 六个阶段

| 阶段 | 产出 |
|---|---|
| 0 建档 | `profile.md`、`target.md`——能从简历解析的就不问你 |
| 1 差距分析 | 统计 5-10 个真实岗位的要求频次；差距分为 `wording` / `cheap` / `structural` |
| 2 背景提升 + 刷题 | 带绝对日期的 `plan.md`；每一项都必须对应阶段 1 的某个差距 |
| 3 简历 | 一份 master，每次投递生成一份定制版，投前过 ATS lint |
| 4 找岗 | `jobs.csv`，每个岗位一个 0-100 匹配分 |
| 5 投递 | 每岗一个包：简历、cover letter、筛选题答案、逐字段填表说明 |
| 6 复盘 | 每周回复率复盘，附明确的决策规则 |

## 边界在哪里

skill 会帮你把申请表填好——上传简历、填联系方式、起草自由回答题。默认在最后那个
默认在最后提交按钮前停下；你一次授权一个批次后，它可以在最终检查通过时自动逐个提交。

法律声明题始终留给你：

- **法律声明题**——工作许可、签证状态、犯罪记录、是否在本公司工作过。这些填错
  可能在你签约之后导致 offer 作废，所以它们会保持空白直到你亲自填。

它同样不会注册账号、登录、经手凭据或支付信息、过 CAPTCHA，也不会在简历上写你
没说过的东西。

自动提交按批次授权，但仍不会登录、绕过 CAPTCHA、填写法律声明题，或处理
支付和完整证件信息。

## 许可

MIT，见 `LICENSE`。
