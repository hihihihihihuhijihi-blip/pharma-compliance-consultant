# 医药合规顾问 · Pharma Compliance Consultant

当前版本 **2.2.1**，由 hbwl 维护。协助医药业务项目判断、合同与制度审查、法规及处罚案例检索、合规体系建设。

## 命令安装：Codex、Claude Code、Cursor

先安装 Node.js，再执行以下命令，按提示选择平台：

```bash
npx skills add hihihihihihuhijihi-blip/pharma-compliance-consultant --skill pharma-compliance-consultant -g
```

安装后启动新会话。Claude Code 输入 `/pharma-compliance-consultant`；Cursor、Codex 桌面端输入 `/` 并选择该技能。Codex CLI/IDE 通过 `/skills` 选择或使用 `$pharma-compliance-consultant`。本包只注册一个技能入口。

[skills 安装工具说明](https://github.com/vercel-labs/skills)。需要查询原文摘录时，平台须能执行 Python 3 脚本或访问 HTTPS JSON。

## 豆包工作：下载 ZIP 导入

从 [最新 Release](https://github.com/hihihihihihuhijihi-blip/pharma-compliance-consultant/releases/latest) 下载资产 `pharma-compliance-consultant.zip`，在豆包工作技能管理中上传完整 ZIP。然后输入 `/`，选择个人中的 `Pharma Compliance Consultant`。

更新已有安装时，优先使用原技能的更新入口；避免同时保留个人导入与本地自动发现的两个同名副本。Release 中的 ZIP 保持完整技能目录结构。

也可使用 [固定下载入口](https://skills.compliances.cc/pharma-compliance-consultant.zip)。

## 知识查询与更新

技能包包含判断准则、工作流程、四张专题卡片、已登记资料索引和查询脚本。原件不在此仓库或 ZIP 中；公开查询返回相关文字和引用，无需另配 MCP。只发送通用检索词，不上传合同、病例、患者信息或内部数据。

原件资料更新后，查询接口读取最新登记资料；技能规则与卡片更新后，需更新已安装副本：命令安装可用 `npx skills update pharma-compliance-consultant`；豆包下载新版 ZIP 并更新原技能。已导入的 ZIP 不会自动替换。

当前查询服务运行在维护者 Mac，经 Cloudflare 提供固定入口；Mac 和网络需保持在线。服务不可用或资料没有可提取正文时，回答会说明未核验范围。

## 使用与文件

允许下载安装和使用本技能。资料引用保留各自来源与适用边界，公开查询不提供原件下载。

完整说明见 [技能 README](pharma-compliance-consultant/README.md) 与 [安装与接入](pharma-compliance-consultant/安装与接入.md)。
