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

## 动态路由矩阵对照表 (Routing Decision Matrix)

| 任务输入类型 | 主激活专家 (Weight: 0.6) | 辅激活专家 (Weight: 0.4) | 核心注入的公理 |
|---|---|---|---|
| **企业宣传 / 招商文案 / 营销脚本** | `game-theory` (昂贵信号) | `cognitive-neuro` (PKM & 递质) | 扎哈维昂贵信号、三元递质回路、反防御性自证 |
| **系统架构 / 关键算法 / 接口设计** | `information-physics` (香农熵减) | `complex-systems` (控制与演化) | 状态机有限性、幂等性公理、故障域隔离、盖尔定律 |
| **商业模式 / 组织分润 / 激励机制** | `economics-pareto` (帕累托最优) | `game-theory` (博弈均衡) | 帕累托前沿外推、逆向选择防范、激励相容、护城河 |
| **复杂决策 / 战略规划 / 危机应对** | `complex-systems` (系统动力学) | `logical-razors` (芒格逆向思维) | 二阶思维、增强回路与瓶颈律、洛拉帕卢扎效应、四大剃刀 |
| **社群运营 / 品牌心智 / 团队领导力** | `evolutionary-social` (社会脑) | `cognitive-neuro` (共情编码) | 敦巴声波梳毛假说、互惠利他同盟、红皇后动态适应 |

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
