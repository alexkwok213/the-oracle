# 门控路由器引擎规范 (Gating Router Protocol)

门控路由器（Router）是 The Oracle 的认知中枢。它的使命是：**拒绝被用户提问中的表层行话（Buzzwords）所蒙蔽，瞬间穿透到事物发生相互作用的底层物理与心智矛盾，并激活加权专家模型。**

---

## 路由识别三问 (The 3 Diagnostic Questions)

当任何输入（待优化的技能、一段待重写的代码、一篇公文草稿）进入 Router 时，算法自动运行以下三问：

### 1. 作用对象问：本任务的核心作用场域是什么？
* **人与人之间的博弈？**（信任、购买、合伙、说服） $\rightarrow$ 路由至：`game-theory` + `cognitive-neuro` + `evolutionary-social`
* **人与机器/系统的交互？**（代码、架构、接口、数据流） $\rightarrow$ 路由至：`information-physics` + `cybernetics-systems`
* **多主体资源的分配与交换？**（激励机制、平台规则、商业模式） $\rightarrow$ 路由至：`economics-pareto` + `game-theory`

### 2. 熵增风险问：当前系统的最大失效模式是什么？
* **信道被噪声淹没？**（公文大词、废话连篇、抽象论文腔） $\rightarrow$ 权重拉满：`information-physics` (香农熵减)
* **引发听众本能排斥？**（自吹自嗨、拉踩同行、自证清白） $\rightarrow$ 权重拉满：`cognitive-neuro` (说服知识模型 PKM) 与 `game-theory` (昂贵信号)
* **系统发生级联雪崩？**（单点脆弱性、未处理边界） $\rightarrow$ 权重拉满：`cybernetics-systems` (故障域隔离)

### 3. 约束条件问：不可逾越的硬边界是什么？
* **法律与合规红线？**（民商法合同责任、广告法） $\rightarrow$ 启动严格合规脱敏约束；
* **生理与认知带宽极限？**（人类听觉语音回路 1.5~2 秒、视觉注意力 3 秒） $\rightarrow$ 启动认知负荷硬约束；
* **系统资源算力/吞吐极限？** $\rightarrow$ 启动复杂度守恒约束。

---

## 动态路由矩阵对照表 (Routing Decision Matrix - 20 Grand Domains)

| 任务输入类型 | 主激活专家 (Weight: 0.6) | 辅激活专家 (Weight: 0.4) | 核心注入的公理 |
|---|---|---|---|
| **辩证分析 / 矛盾调和 / 质变相变** | `dialectical-thinking` (辩证思维) | `complex-systems` (控制与演化) | 黑格尔正反合扬弃律 (Aufheben)、三大辩证规律、苏格拉底反诘法、物极必反、玻姆深度汇谈 |
| **批判性审视 / 严密论证 / 逻辑打假** | `critical-reasoning` (批判性思维) | `logical-razors` (逻辑剃刀) | 保罗-埃尔德8要素与9标准、图尔敏6要素论证骨架、皮尔士溯因法、全量逻辑谬误解构 |
| **平台伦理 / 契约公平 / 制度正义** | `ethics-social-contract` (伦理契约) | `economics-pareto` (帕累托最优) | 罗尔斯无知之幕、最大最小原则 (Maximin)、康德人是目的公理、正向外部性、道德风险对冲 |
| **破框思考 (Think Out of the Box) / 颠覆创新** | `lateral-breakthrough` (横向思维) | `complex-systems` (二阶改变) | 九点隐性假设粉碎、瓦茨拉维克二阶改变、TRIZ四大矛盾分离、PO挑衅算子、正交升维 |
| **元认知排查 / 认知偏差 / 避免做蠢事** | `epistemic-latticework` (认知格栅) | `logical-razors` (逻辑剃刀) | 地图不是疆域、查理·芒格25种误判心理学、能力圈边界、局部最优模拟退火跳跃 |
| **企业宣传 / 招商文案 / 营销脚本** | `game-theory` (昂贵信号) | `semiotics-language` (符号与言语行为) | 扎哈维昂贵信号、奥斯汀言语行为、皮尔斯指示符号、反防御性自证 |
| **视频视听脚本 / 分镜与剪辑规划** | `multimodal-physics` (音画物理) | `cognitive-neuro` (双重编码) | 普多夫金音画对位律、视网膜切率极限 (1.5~4s)、声学侧链闪避 |
| **用户心智决策 / 转化率 / 定价机制** | `behavioral-heuristics` (行为经济) | `cognitive-neuro` (三元递质回路) | 卡尼曼双系统模型、前景理论损失厌恶、框架效应、心理账户 |
| **系统架构 / 关键算法 / 分布式协同** | `computation-network` (计算与网络) | `information-physics` (香农熵减) | 图灵停机边界、P vs NP 剪枝、CAP 定理、有限状态机幂等性 |
| **商业模式 / 组织分润 / 激励机制** | `economics-pareto` (帕累托最优) | `antifragility-security` (机制安全) | 帕累托前沿外推、逆向选择防范、激励相容、肌肤之亲公理 |
| **竞争对抗 / 破局打法 / 战略推演** | `strategy-ooda` (大战略博弈) | `complex-systems` (控制与演化) | 博伊德 OODA 环、重心法则 (Schwerpunkt)、奇正相生、破坏性创新 |
| **组织韧性 / 长期运营 / 跨越周期** | `thermodynamics-statistical` (热力学) | `antifragility-security` (反脆弱) | 玻尔兹曼负熵流、耗散结构自组织、遍历性破产吸收态守护、凸性效应 |
| **数据分析 / 效果归因 / 功效验证** | `causality-bayes` (因果与贝叶斯) | `logical-razors` (哲学剃刀) | 珀尔因果梯三层模型、混杂因子隔离、贝叶斯先验似然比、萨根标准 |
| **复杂决策 / 宏观战略 / 盲区排查** | `complex-systems` (系统动力学) | `logical-razors` (芒格逆向思维) | 盖尔定律、二阶思维 (And then what?)、洛拉帕卢扎效应、四大剃刀 |
| **社群网络 / 裂变增长 / 部落共鸣** | `evolutionary-social` (社会脑) | `computation-network` (无标度网络) | 敦巴声波梳毛假说、互惠利他同盟、无标度网络中心节点、红皇后假说 |
| **语言表达 / 黑话洗净 / 概念普及** | `semiotics-language` (语言哲学) | `behavioral-heuristics` (启发式) | 维特根斯坦语言游戏说、莱考夫身体化隐喻、系统1直觉穿透 |

---

## 路由输出规范 (Router Output Contract)

门控路由器完成分析后，必须向执行合成器输出标准 JSON 格式的元指令：

```json
{
  "router_diagnosis": {
    "detected_domain": "商业心智与信任建立",
    "core_conflict": "平台急于建立信任，但使用廉价口号与自证清白，触发了受众的PKM反营销免疫防御",
    "primary_experts": [
      "game-theory.CostlySignaling",
      "cognitive-neuro.PersuasionKnowledgeModel"
    ],
    "secondary_experts": [
      "information-physics.ShannonSNR",
      "economics-pareto.ParetoImprovement"
    ],
    "pareto_invariants": [
      "感染力不得低于原版基准",
      "企业格局不得降级为地摊小作坊"
    ]
  }
}
```
