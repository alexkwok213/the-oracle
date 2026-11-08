# The Oracle: 基于第一性原理的公理级 MoE 技能架构与元优化引擎

> **“先知不制造套路，先知洞悉统治宇宙与人类心智的客观公理。”**  
> **Axiomatic MoE Meta-Skill Engine powered by First Principles, Game Theory, Information Physics & Pareto Optimality.**

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)
[![Architecture: MoE Engine](https://img.shields.io/badge/Architecture-Axiomatic%20MoE-blue.svg)](SKILL.md)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](core/router.md)

---

## 🌌 为什么需要 The Oracle？

市面上现有的 Prompt / 技能优化工具，99% 都困在**“表层语法与技巧（Syntax & Tricks）”**中：
* 加角色设定（You are an expert...）
* 加思维链（Think step by step...）
* 加输出格式限制（Output JSON only...）

**当面对复杂的现实商业世界、深层人心博弈与高危系统工程时，这些表面技巧瞬间失效。**

**The Oracle** 彻底颠覆了这种传统做法。它不是一个机械的“流程生成器”（像传统的 skill-creator），而是一个**内置了世界运转底层规律的“先知型 MoE 认知编译器”**：
1. **透过现象看本质**：通过**门控路由器 (Gating Router)**，瞬间剥离行话，洞悉深层矛盾；
2. **底层公理专家池**：自动调度物理学、博弈论、神经生物学、演化论、经济学的底层公理；
3. **帕累托仲裁器**：严禁“拆东墙补西墙”式的负优化，确保任何改进都是无副作用的绝对升维；
4. **三维红队测试**：经历怀疑者、法务极客与过度修正仲裁官的饱和式攻击，打造免检级系统。

---

## 🏛 架构全景 (System Architecture)

```mermaid
flowchart TD
    User[用户输入: 任何需要优化的技能 / 复杂任务 / 初稿] --> Router[门控路由器 Router: 核心矛盾特征解构]
    
    subgraph 底层公理专家池 Expert Axiom Pool (30 Grand Domains / 150 Models)
        E1[博弈论与演化专家: 昂贵信号 / 纳什均衡 / 梳毛假说]
        E2[物理与信息论专家: 香农熵减 / 高信噪比 / 复杂度守恒]
        E3[认知与神经科学专家: PKM模型 / 双重编码 / 递质回路]
        E4[经济学与运筹专家: 帕累托最优 / 边际递减 / 护城河]
        E5[演化生物与生态专家: 梳毛假说 / 红皇后效应 / 生态位隔离]
        E6[复杂系统与控制论专家: 反馈回路 / 盖尔定律 / 二阶思维]
        E7[逻辑剃刀与芒格心智专家: 逆向思维 / 洛拉帕卢扎效应 / 四大剃刀]
        E8[因果革命与贝叶斯专家: 珀尔因果梯 / 混杂隔离 / 贝叶斯似然比]
        E9[反脆弱性与机制安全专家: 凸性效应 / 肌肤之亲公理 / 拜占庭容错]
        E10[多模态视听物理专家: 普多夫金音画对位 / 视网膜切率 / 声学侧链]
        E11[行为经济与认知启发专家: 双系统 / 前景理论损失厌恶 / 心理账户]
        E12[计算理论与网络科学专家: 图灵停机边界 / P vs NP / 无标度网络]
        E13[大战略博弈与OODA环专家: OODA循环 / 重心法则 / 破坏性创新]
        E14[热力学与统计物理专家: 玻尔兹曼负熵流 / 耗散结构 / 遍历性破产防范]
        E15[语言哲学与符号学专家: 维特根斯坦语言游戏 / 言语行为 / 认知隐喻]
        E16[破框思维与TRIZ矛盾分离专家: 九点隐性假设 / 二阶改变 / 矛盾分离 / 正交升维]
        E17[认知格栅与人类误判学专家: 地图不是疆域 / 芒格25种偏见 / 模拟退火跳跃]
        E18[辩证思维与对立统一专家: 黑格尔正反合扬弃 / 质量互变 / 苏格拉底反诘 / 东方阴阳]
        E19[批判性思维与论证逻辑专家: 保罗-埃尔德模型 / 图尔敏6要素论证 / 逻辑谬误解构]
        E20[伦理契约与罗尔斯正义专家: 无知之幕 / 最大最小公理 Maximin / 康德人是目的]
        E21[系统基模与干预杠杆专家: 梅多斯12大杠杆点 / 舍本逐末 / 成长上限 / 目标侵蚀]
        E22[精益实验与刻意练习专家: 多臂老虎机UCB / MVP飞轮 / 费曼测试 / 心理表征]
        E23[叙事动力学与峰终美学专家: 坎贝尔英雄之旅 / 三幕剧净化 / 蔡加尼克悬念 / 峰终定律]
        E24[范畴同构与战略不变量专家: 范畴论函子映射 / 诺特十年不变量 / 韦斯特规模幂律 / 奇异环]
        E25[东方古典兵学与阳明心学专家: 先胜求战 / 避实击虚 / 奇正相生 / 反者道之动 / 知行合一]
        E26[量子认识论与叠加态决策专家: 海森堡观察者效应 / 波粒二象性 / 战略叠加态 / 路径积分]
        E27[制度经济学与康威拓扑专家: 科斯交易成本 / 诺斯路径依赖 / 奥斯特罗姆公地治理 / 康威定律]
        E28[流行病模因与心理免疫专家: R0裂变公式 / 道金斯模因论 / 麦圭尔心理疫苗 / 复杂传染宽桥]
        E29[认知工效学与极简美学专家: 希克定律 / 菲茨定律 / 拉姆斯极简十诫 / MAYA原理与留白负熵]
        E30[科学革命与从0到1创造专家: 库恩范式转移 / 拉卡托斯硬核保护带 / 熊彼特创造性破坏 / 蒂尔秘密]
    end
    
    Router -->|动态加权路由| E1 & E2 & E3 & E4 & E5 & E6 & E7 & E8 & E9 & E10 & E11 & E12 & E13 & E14 & E15 & E16 & E17 & E18 & E19 & E20 & E21 & E22 & E23 & E24 & E25 & E26 & E27 & E28 & E29 & E30
    
    E1 & E2 & E3 & E4 & E5 & E6 & E7 & E8 & E9 & E10 & E11 & E12 & E13 & E14 & E15 & E16 & E17 & E18 & E19 & E20 & E21 & E22 & E23 & E24 & E25 & E26 & E27 & E28 & E29 & E30 --> Synthesizer[第一性原理熔铸与解法重构]
    
    subgraph 质检与自举演化引擎
        Synthesizer --> Pareto[帕累托天平: 零负优化与反古德哈特作弊仲裁]
        Pareto --> RedTeam[可执行三维红队对抗审查: 怀疑者+法务猎人+反白开水审美官]
        RedTeam --> Bootstrapping[递归自指演化引擎: TOC逐代瓶颈击穿至不动点]
    end
    
    Bootstrapping --> Output[输出: 跨学科第一性原理驱动的免检级终极技能]
```

---

## 🧠 先知专家池核心公理 (The 30 Grand Expert Domains & Top 150 Mental Models)

本体系汲取**查理·芒格多元思维模型格栅 (Latticework of Mental Models)** 与人类前 150 伟大科学理论精髓，构建了 30 大不可动摇的公理专家池：

| 专家模块 | 第一性原理 | 核心公理推导 | 解决的问题 |
|---|---|---|---|
| [`experts/game-theory.md`](experts/game-theory.md) | **扎哈维昂贵信号 & 重复博弈** (Costly Signaling) | 廉价吹牛成本为零，理智受众本能免疫；唯有高成本质押的昂贵信号能建立不可伪造的信任；打破囚徒困境 | 消除自嗨自夸、短期割韭菜倾向 |
| [`experts/information-physics.md`](experts/information-physics.md) | **香农信息论与高信噪比** (Shannon SNR) | 信息的本质是消除不确定性（熵减）；公文大词是高熵噪音，必须降维为具体事实画面；复杂度守恒律 | 消除抽象空洞、废话连篇、认知过载 |
| [`experts/cognitive-neuro.md`](experts/cognitive-neuro.md) | **三元递质回路 & PKM** (Neurochemical Triad) | 决策由神经递质主导：皮质醇唤醒警觉 $\rightarrow$ 催产素唤醒同盟归属 $\rightarrow$ 多巴胺唤醒未来奖赏渴望；双重编码理论 | 解决心智防御、无法促成行动 |
| [`experts/economics-pareto.md`](experts/economics-pareto.md) | **帕累托改进与经济护城河** (Pareto & Moats) | 优化必须在不损害任何核心维度的前提下让某维度更好；机会成本第一定律；边际成本递减；无形资产护城河 | 防止过度修正、白开水陷阱 |
| [`experts/evolutionary-social.md`](experts/evolutionary-social.md) | **敦巴声波梳毛 & 红皇后效应** (Social Brain) | 语言的演化本质是替代身体梳毛建立同盟；红皇后动态适应；高斯排斥原理生态位分化 | 消除公文距离感、同质化内卷竞争 |
| [`experts/complex-systems.md`](experts/complex-systems.md) | **盖尔定律与二阶思维** (Complex Systems) | 复杂系统必由简单微闭环演化而来；正负反馈回路平衡；临界质量相变；约束理论击穿唯一瓶颈 | 杜绝臃肿设计、短视一阶思维 |
| [`experts/logical-razors.md`](experts/logical-razors.md) | **芒格逆向思维 & 四大剃刀** (Inversion & Razors) | 倒过来想（先消灭死因）；洛拉帕卢扎多重心理共振；激励超级反应；奥卡姆/汉隆/萨根/希钦斯四大哲学剃刀 | 排查认知盲区、防范虚假宣称 |
| [`experts/causality-bayes.md`](experts/causality-bayes.md) | **珀尔因果革命与贝叶斯理性** (Causality & Bayes) | 珀尔因果梯三层模型（关联-干预-反事实）；混杂因子隔离；后此谬误防范；贝叶斯先验似然比更新 | 数据虚假归因、把巧合当因果 |
| [`experts/antifragility-security.md`](experts/antifragility-security.md) | **塔勒布反脆弱性与机制安全** (Antifragility & Skin in the Game) | 凸性效应（非对称收益）；肌肤之亲公理（权责对称，自担风险）；拜占庭容错与防投机刷单 | 机制脆弱、搭便车与系统崩溃 |
| [`experts/multimodal-physics.md`](experts/multimodal-physics.md) | **视听物理学与多模态流媒体** (Multimodal Physics) | 普多夫金音画对位律；视网膜认知切率极限（1.5~4秒）；声学掩蔽与侧链闪避；耳蜗工作记忆气口律 | 视频音画脱节、视觉疲劳、窒息长句 |
| [`experts/behavioral-heuristics.md`](experts/behavioral-heuristics.md) | **行为经济学与认知启发式** (Behavioral Heuristics) | 卡尼曼双系统模型 (System 1/2)；前景理论非对称损失厌恶 (2.5x)；框架效应与心理账户；默认选项助推 | 忽视人类非理性心理防线、转化率低迷 |
| [`experts/computation-network.md`](experts/computation-network.md) | **计算理论与网络科学** (Computation & Network) | 图灵停机问题不可判定性；P vs NP 启发式剪枝；无标度网络幂律分布与关键 Hub 节点；CAP 定理 | 算法失控死锁、盲目枚举、流量裂变无重心 |
| [`experts/strategy-ooda.md`](experts/strategy-ooda.md) | **动态博弈大战略与OODA环** (Grand Strategy & OODA) | 约翰·博伊德 OODA 动态决策环；克劳塞维茨重心法则 (Schwerpunkt)；奇正相生；克里斯坦森破坏性创新 | 错失战机、反应迟钝、多头出击无突破口 |
| [`experts/thermodynamics-statistical.md`](experts/thermodynamics-statistical.md) | **热力学、统计物理与遍历性** (Thermodynamics & Ergodicity) | 玻尔兹曼负熵流（对抗内卷衰亡）；普里戈金耗散结构自组织；遍历性认识论（严禁踩踏破产吸收态） | 组织僵化死亡、违法踩雷致命吸收态 |
| [`experts/semiotics-language.md`](experts/semiotics-language.md) | **语言哲学与认知隐喻** (Semiotics & Language) | 维特根斯坦“语言游戏说”（意义即用法）；奥斯汀言语行为理论（以言行事）；皮尔斯指示符号；概念隐喻 | 沉迷大词黑话、假大空自嗨、无法建立通感 |
| [`experts/lateral-breakthrough.md`](experts/lateral-breakthrough.md) | **破框思维与TRIZ矛盾分离** (Lateral & Out-of-the-Box) | 九点隐性假设粉碎律；瓦茨拉维克二阶改变（跳出系统本身）；德博诺 PO 挑衅算子；TRIZ四大矛盾分离；正交升维 | 思维撞墙、落入平庸妥协折中、局限在系统内部修补 |
| [`experts/epistemic-latticework.md`](experts/epistemic-latticework.md) | **认知格栅与人类误判学** (Epistemic Latticework) | 地图不是疆域；查理·芒格25种误判心理学（证实偏见/不一致规避/权威从众）；能力圈边界；模拟退火全局跃迁 | 误判现实、过度自信、被困在局部最优小山丘 |
| [`experts/dialectical-thinking.md`](experts/dialectical-thinking.md) | **辩证思维与对立统一扬弃** (Dialectical Thinking) | 黑格尔正反合扬弃律 (Aufheben)；对立统一/质量互变/否定之否定三大规律；苏格拉底反诘法；东方阴阳物极必反；戴维·玻姆深度汇谈 | 认知非黑即白死板分裂、不会调和深层矛盾、缺乏战略耐心 |
| [`experts/critical-reasoning.md`](experts/critical-reasoning.md) | **批判性思维与图尔敏论证** (Critical Reasoning) | 保罗-埃尔德8思维要素与9严苛智力标准；图尔敏论证六要素（主张/数据/保证/支撑/限定/反驳）；皮尔士溯因法；20+逻辑谬误解构 | 逻辑漏洞百出、偷换概念自欺欺人、轻信伪科学谎言 |
| [`experts/ethics-social-contract.md`](experts/ethics-social-contract.md) | **伦理契约与罗尔斯正义** (Ethics & Social Contract) | 罗尔斯“无知之幕”；最大最小公理 (Maximin)；康德绝对命令（人是目的而非工具）；正外部性社会福利函数；委托代理道德风险对冲 | 掠夺式分润机制、丧失道德合法性、割韭菜引发生态暴雷 |
| [`experts/system-archetypes.md`](experts/system-archetypes.md) | **系统基模与干预杠杆点** (System Archetypes & Leverage) | 德内拉·梅多斯12大系统干预杠杆点；圣吉舍本逐末/饮鸩止渴基模；成长上限；目标侵蚀；公地悲剧 | 治标不治本、短期止痛药成瘾、低杠杆参数微调无效 |
| [`experts/lean-experimentation.md`](experts/lean-experimentation.md) | **精益实验与刻意练习** (Lean & Deliberate Practice) | 多臂老虎机探索-利用权衡 (UCB)；精益创业构建-测量-学习飞轮；费曼学习法去术语测试；艾利克森刻意练习与心理表征 | 闭门造车盲目投入、术语伪装不懂装懂、机械重复无长进 |
| [`experts/narrative-aesthetics.md`](experts/narrative-aesthetics.md) | **叙事动力学与峰终美学** (Narrative & Peak-End) | 坎贝尔英雄之旅与智者导师定位；亚里士多德三幕剧与卡塔西斯净化；蔡加尼克悬念闭合律；卡尼曼峰终定律 | 品牌自嗨抢当主角、平铺直叙无悬念、结尾平庸无记忆点 |
| [`experts/category-isomorphism.md`](experts/category-isomorphism.md) | **范畴同构与战略不变量** (Category Isomorphism & Invariants) | 范畴论函子同构映射；诺特定理与贝索斯十年战略不变量；韦斯特规模法则幂律；冯·诺依曼自复制奇异环 | 跨学科壁垒割裂、追逐短期风口、组织规模膨胀死于官僚热寂 |
| [`experts/eastern-strategy-philosophy.md`](experts/eastern-strategy-philosophy.md) | **东方古典兵学与阳明心学** (Eastern Strategy & Yangming) | 《孙子兵法》先胜而后求战/致人而不致于人/避实击虚/奇正相生；老子反者道之动；王阳明知行合一与事上磨练 | 陷入同质化正面肉搏、自夸强梁惹人反感、知而不行假把式 |
| [`experts/quantum-epistemology.md`](experts/quantum-epistemology.md) | **量子认识论与叠加态决策** (Quantum Epistemology) | 海森堡测不准与观察者效应；玻尔波粒二象互补原理；薛定谔战略叠加态与延迟坍缩；费曼路径积分相长干涉 | 传统调研问卷被印象管理欺骗、过早赌死单一路径、表达缺乏波粒双模态张力 |
| [`experts/institutional-governance.md`](experts/institutional-governance.md) | **制度经济学与康威拓扑** (Institutional Economics & Conway) | 科斯定理与交易成本边界；诺斯制度路径依赖破解；奥斯特罗姆自主治理8原则；康威定律与逆康威操作 | 平台未能替个体抹平交易摩擦、被历史路径依赖锁死、部门墙导致架构臃肿 |
| [`experts/epidemiology-memetics.md`](experts/epidemiology-memetics.md) | **流行病模因与心理免疫** (Epidemiology & Inoculation) | 流行病学 $R_0 = \beta c d$ 裂变公式；道金斯模因论三定律；麦圭尔心理免疫接种理论；森托拉复杂传染宽桥定律 | 传播链无法自发裂变、一句话记不住传不开、遇外部一句质疑就信任崩盘 |
| [`experts/design-aesthetics-physics.md`](experts/design-aesthetics-physics.md) | **认知工效学与极简美学** (Interaction Physics & Aesthetics) | 希克-海曼决策熵定律（单一CTA）；菲茨可达性定律；迪特·拉姆斯极简十诫；罗维MAYA原理与留白负熵律 | 选项过多导致用户决策瘫痪、转化路径繁琐、装饰冗余淹没核心金句 |
| [`experts/paradigm-revolutions.md`](experts/paradigm-revolutions.md) | **科学革命与从0到1创造** (Paradigm Revolutions & 0-to-1) | 托马斯·库恩范式转移与不可通约性；拉卡托斯硬核与保护带纲领；熊彼特创造性破坏；彼得·蒂尔从0到1反共识秘密 | 在旧范式里造更圆的马车轮子、妥协丧失核心公理硬核、水平模仿无反共识秘密 |

---

## ⚖️ 帕累托改进仲裁铁律

$$\Delta \text{Skill} \ge 0 \quad (\forall i \in \text{Core Dimensions}: \Delta D_i \ge 0 \quad \land \quad \exists j: \Delta D_j > 0)$$

1. **绝对禁令**：严禁“为了合规牺牲气场”、“为了接地气降级为地摊小作坊”；
2. **升维跃迁**：遭遇两难对立时，严禁折中妥协，必须引入高维锚点（如百强药企沉淀、国家特医批文）直接推升帕累托最优边界！

---

## 📁 项目目录索引

```
the-oracle/
├── SKILL.md                      # 核心元技能定义规范（Agent 原生支持，自评 100.0/100）
├── README.md                     # 项目哲学全景与架构说明
├── core/                         # 核心控制中枢
│   ├── router.md                 # 门控路由引擎协议 (30 Grand Domains)
│   ├── pareto-arbiter.md         # 帕累托改进仲裁器 (含反古德哈特作弊防线)
│   ├── red-team.md               # 三维红队对抗攻击协议
│   └── bootstrapping.md          # 递归自指自举进化协议 (v1.0 -> v3.0 完整演化台账)
├── experts/                      # 先知公理专家池 (The 30 Grand Domains)
│   ├── game-theory.md            # 01. 博弈论与昂贵信号专家
│   ├── information-physics.md    # 02. 物理与信息控制论专家
│   ├── cognitive-neuro.md        # 03. 认知神经科学专家
│   ├── economics-pareto.md       # 04. 微观经济学与帕累托专家
│   ├── evolutionary-social.md    # 05. 演化生物学与社会学专家
│   ├── complex-systems.md        # 06. 复杂系统与控制论专家
│   ├── logical-razors.md         # 07. 哲学逻辑剃刀与芒格心智专家
│   ├── causality-bayes.md        # 08. 珀尔因果革命与贝叶斯专家
│   ├── antifragility-security.md # 09. 反脆弱与机制安全公理专家
│   ├── multimodal-physics.md     # 10. 多模态视听物理模型专家
│   ├── behavioral-heuristics.md  # 11. 行为经济学与认知启发式专家
│   ├── computation-network.md    # 12. 计算理论与网络拓扑学专家
│   ├── strategy-ooda.md          # 13. 动态博弈大战略与OODA环专家
│   ├── thermodynamics-statistical.md # 14. 热力学、统计物理与遍历性专家
│   ├── semiotics-language.md     # 15. 语言哲学与认知符号学专家
│   ├── lateral-breakthrough.md   # 16. 破框思维、横向跳跃与TRIZ矛盾分离专家
│   ├── epistemic-latticework.md  # 17. 认知格栅、元认识论与人类误判学专家
│   ├── dialectical-thinking.md   # 18. 辩证思维与对立统一扬弃专家
│   ├── critical-reasoning.md     # 19. 批判性思维与图尔敏论证专家
│   ├── ethics-social-contract.md # 20. 伦理契约与罗尔斯正义公理专家
│   ├── system-archetypes.md      # 21. 系统基模与梅多斯干预杠杆点专家
│   ├── lean-experimentation.md   # 22. 精益实验、多臂老虎机与刻意练习专家
│   ├── narrative-aesthetics.md   # 23. 叙事动力学、英雄之旅与峰终美学专家
│   ├── category-isomorphism.md   # 24. 范畴同构、规模法则与战略不变量专家
│   ├── eastern-strategy-philosophy.md # 25. 东方古典兵学、道家演化与阳明心学专家
│   ├── quantum-epistemology.md   # 26. 量子认识论、观察者效应与叠加态决策专家
│   ├── institutional-governance.md # 27. 制度经济学、交易成本与康威拓扑专家
│   ├── epidemiology-memetics.md  # 28. 流行病学、模因裂变与心理免疫接种专家
│   ├── design-aesthetics-physics.md # 29. 认知工效学、交互物理学与极简美学专家
│   └── paradigm-revolutions.md   # 30. 科学革命、范式转移与从0到1创造专家
├── scripts/                      # 自动化确定性工程工具链 (Zero Dependencies)
│   ├── oracle_compiler.py        # 全链路认知编译器 & 哥德尔全仓自指审计器 (--self-audit-repo)
│   ├── oracle_router.py          # 可执行门控路由调度引擎 (30 Experts / 150 Models)
│   ├── oracle_eval.py            # 跨领域公理量化评估与反古德哈特帕累托仲裁器 (5 Domains)
│   ├── oracle_redteam.py         # 可执行三维红队对抗审讯引擎 (怀疑者/法务极客/反白开水审美官)
│   ├── oracle_mutate.py          # 公理级靶向瓶颈变异与重构算子执行引擎
│   ├── oracle_loop.py            # 递归多代自指进化收敛引擎 (TOC 逐代瓶颈击穿 + 不动点收敛)
│   └── run_oracle_audit.sh       # 7 阶段 CI/CD 自动化回归质检流水线
├── tests/                        # 单元测试套件
│   └── test_oracle_engine.py     # 16 大跨学科公理、反作弊、红队与递归进化单元测试 (100% 通过)
├── references/                   # 权威经典参考指南
│   └── top-100-mental-models.md  # 人类前 150 伟大思维模型与理论全景索引 (15 章全覆盖)
└── benchmarks/                   # 黄金通关标杆案例
    ├── case-human-article.md     # 商业文案心智重构实战全景
    └── case-agent-skill-evolution.md # Agent 技能架构元进化实战全景 (TOC 逐代瓶颈击穿)
```

---

## 🛠 自动化量化工程工具链使用指引 (CLI Toolkit)

The Oracle v3.0 自带轻量级、零外部依赖的自动化工程套件，支持全链路认知编译、门控路由诊断、单文本评估、三维红队审讯、优化前后帕累托裁决与递归多代自指进化：

```bash
# 0. 一键运行 5 阶段全链路认知编译器 (路由 -> 评估 -> 红队 -> 多代进化 -> 终局裁决)
python3 scripts/oracle_compiler.py dirty_input.txt -o compiled_output.txt

# 1. 运行哥德尔全仓自指健康度审计证书 (校验 30 专家 / 150 模型 / 100分自评 / 红队通关)
python3 scripts/oracle_compiler.py --self-audit-repo

# 2. 可执行门控路由诊断 (自动匹配 30 大先知领域与 150 大思维模型)
python3 scripts/oracle_router.py "你的任务描述或文件路径"

# 3. 可执行三维红队对抗审讯 (三大恶魔代言人逐句挑刺)
python3 scripts/oracle_redteam.py "待审讯文本或文件路径"

# 4. 跨领域公理评估与帕累托仲裁 (支持 copy / code / strategy / skill / reasoning 五大领域)
python3 scripts/oracle_eval.py --before draft_before.txt --after draft_after.txt

# 5. 执行 7 阶段完整自动化回归与质检流水线
./scripts/run_oracle_audit.sh
```

---

## 🚀 如何安装与调用

### 作为 Agent 技能集成
直接将本目录软链接到你的 Agent 技能目录（支持 Antigravity / Claude Code / Codex）：
```bash
ln -s /path/to/the-oracle ~/.gemini/antigravity/skills/the-oracle
```

### 调用模式
当面对复杂任务或需要优化已有技能时，直接指示 Agent：
> *“请调用 The Oracle 引擎，识别当前任务的核心矛盾，激活对应的底层公理专家，执行帕累托改进与红队对抗测试。”*

---

## 📄 License

MIT License - 传承第一性原理，让人工智能触碰世界底层的确定性。
