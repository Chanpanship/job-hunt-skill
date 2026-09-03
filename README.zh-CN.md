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

## 先看效果

`DEMO.md` 用 `demo/workspace/` 里一个虚构案例走完了整个流程，附真实脚本输出——
包括一处**工具自己的指标反而奖励了更差的简历**。试试：

```bash
python .claude/skills/job-hunt/scripts/ats_check.py demo/workspace/resume/v1-before.md --jd demo/workspace/jobs/jd/grabbish-mle.txt
```

那份简历会得到 1 个 error、17 个 warning。用同样的事实重写的定制版是零。

## 开始用

在 Claude Code 里，于项目目录下：

```bash
claude "帮我找工作，我的简历在 <路径>"
```

在 Codex CLI 里：

```bash
codex "读 AGENTS.md，然后用 <路径> 的简历开始阶段 0"
```

之后就是正常对话。状态存在 `workspace/`，所以下次开会话是接着走，而不是重新问你一遍。

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

## 追踪

```bash
python .claude/skills/job-hunt/scripts/jobs_db.py add --company "Acme" --title "ML Engineer" --source greenhouse --fit 82
```

```bash
python .claude/skills/job-hunt/scripts/jobs_db.py stats
```

投了 30 份回复率低于 5% 时，`stats` 会直接告诉你去改简历或改目标，而不是继续加量。

## 它不会做的事

不会替你提交申请、发消息、注册账号、过 CAPTCHA、把你的个人信息填进网站，也不会
在简历上写你没说过的东西。它把一切准备好，**由你按下提交**。

这是有意为之。自动提交会导致账号被封、会把 A 公司的简历投给 B 公司，而且工作许可、
犯罪记录、前雇主这类法律声明题只有你本人能回答。

## 隐私

`workspace/` 存的是你真实的简历、联系方式和投递记录，已被 gitignore 排除。不要提交
它，也建议想清楚再把这个文件夹放进会同步到云端的目录。

## 许可

MIT，见 `LICENSE`。
