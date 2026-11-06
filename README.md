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
    
    subgraph 底层公理专家池 Expert Axiom Pool (10 Grand Domains)
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
    end
    
    Router -->|动态加权路由| E1 & E2 & E3 & E4 & E5 & E6 & E7 & E8 & E9 & E10
    
    E1 & E2 & E3 & E4 & E5 & E6 & E7 & E8 & E9 & E10 --> Synthesizer[第一性原理熔铸与解法重构]
    
    subgraph 质检与自举演化引擎
        Synthesizer --> Pareto[帕累托天平: 零负优化与过度修正仲裁]
        Pareto --> RedTeam[三维红队对抗审查: 极客挑刺+边界破坏]
        RedTeam --> Bootstrapping[递归自指演化引擎: 多代变异迭代至不动点]
    end
    
    Bootstrapping --> Output[输出: 跨学科第一性原理驱动的免检级终极技能]
```

---

## 🧠 先知专家池核心公理 (The 10 Grand Expert Domains)

本体系汲取**查理·芒格多元思维模型格栅 (Latticework of Mental Models)** 与全网顶级认知科学精髓，构建了 10 大不可动摇的公理专家池：

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

---

## ⚖️ 帕累托改进仲裁铁律

$$\Delta \text{Skill} \ge 0 \quad (\forall i \in \text{Core Dimensions}: \Delta D_i \ge 0 \quad \land \quad \exists j: \Delta D_j > 0)$$

1. **绝对禁令**：严禁“为了合规牺牲气场”、“为了接地气降级为地摊小作坊”；
2. **升维跃迁**：遭遇两难对立时，严禁折中妥协，必须引入高维锚点（如百强药企沉淀、国家特医批文）直接推升帕累托最优边界！

---

## 📁 项目目录索引

```
the-oracle/
├── SKILL.md                      # 核心元技能定义规范（Agent 原生支持）
├── README.md                     # 项目哲学全景与架构说明
├── core/                         # 核心控制中枢
│   ├── router.md                 # 门控路由引擎协议
│   ├── pareto-arbiter.md         # 帕累托改进仲裁器
│   ├── red-team.md               # 三维红队对抗攻击协议
│   └── bootstrapping.md          # 递归自指自举进化协议
├── experts/                      # 先知公理专家池 (The 10 Grand Domains)
│   ├── game-theory.md            # 博弈论与昂贵信号专家
│   ├── information-physics.md    # 物理与信息控制论专家
│   ├── cognitive-neuro.md        # 认知神经科学专家
│   ├── economics-pareto.md       # 微观经济学与帕累托专家
│   ├── evolutionary-social.md    # 演化生物学与社会学专家
│   ├── complex-systems.md        # 复杂系统与控制论专家
│   ├── logical-razors.md         # 哲学逻辑剃刀与芒格心智专家
│   ├── causality-bayes.md        # 珀尔因果革命与贝叶斯专家
│   ├── antifragility-security.md # 反脆弱与机制安全公理专家
│   └── multimodal-physics.md     # 多模态视听物理模型专家
├── scripts/                      # 自动化确定性工程工具链 (Zero Dependencies)
│   ├── oracle_eval.py            # 跨领域公理量化评估与帕累托仲裁器 (Copy/Code/Strategy/Skill)
│   ├── oracle_mutate.py          # 公理级变异与重构算子执行引擎
│   ├── oracle_loop.py            # 递归多代自指进化收敛引擎 (TOC 瓶颈诊断 + 不动点收敛)
│   └── run_oracle_audit.sh       # 5 阶段 CI/CD 自动化回归质检流水线
├── tests/                        # 单元测试套件
│   └── test_oracle_engine.py     # 9 大跨学科公理单元测试 (100% 通过)
└── benchmarks/                   # 黄金通关标杆案例
    └── case-human-article.md     # 商业文案心智重构实战全景
```

---

## 🛠 自动化量化工程工具链使用指引 (CLI Toolkit)

The Oracle 自带轻量级、零外部依赖的自动化工程套件，支持单文本评估、优化前后帕累托裁决、公理变异重构与递归自指进化：

```bash
# 1. 跨领域公理评估 (支持 copy / code / strategy / skill 四大领域)
python3 scripts/oracle_eval.py "待评估文本或文件路径"

# 2. 仲裁优化前后的帕累托改进 (是否属于零负优化的绝对跃迁)
python3 scripts/oracle_eval.py --before draft_before.txt --after draft_after.txt

# 3. 执行公理级变异重构 (熵减、合规降维、指令结构化)
python3 scripts/oracle_mutate.py dirty_input.txt -o clean_output.txt

# 4. 运行递归多代自指进化循环 (迭代直至帕累托不动点收敛)
python3 scripts/oracle_loop.py target.txt --max-iter 5 -o evolved.txt

# 5. 执行 5 阶段完整自动化回归与质检流水线
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
