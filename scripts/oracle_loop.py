#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Oracle: Recursive Self-Evolution & Pareto Convergence Loop
Iteratively applies Axiomatic Operators until no Pareto Improvement is possible
(Fixed-Point Convergence to the Pareto Frontier).
"""

import sys
import os
import json
import argparse
from typing import Dict, List, Any, Tuple, Optional

# 引入核心评估、仲裁与变异算子引擎
from oracle_eval import evaluate_universal, arbitrate_pareto, print_universal_report
from oracle_mutate import mutate_text, mutate_by_bottleneck

class RecursiveOracleEngine:
    def __init__(self, domain: str = "auto", max_iterations: int = 6, epsilon: float = 0.5):
        self.domain = domain
        self.max_iterations = max_iterations
        self.epsilon = epsilon
        self.history: List[Dict[str, Any]] = []

    def diagnose_bottleneck(self, evaluation: Dict[str, Any]) -> Tuple[str, str]:
        """基于约束理论 (Theory of Constraints) 寻找当前系统的唯一最大瓶颈"""
        v = evaluation["pareto_vector"]
        sorted_dims = sorted(v.items(), key=lambda x: x[1])
        bottleneck_dim, score = sorted_dims[0]
        
        prescriptions = {
            # Copy Domain
            "impact_signaling": "扎哈维昂贵信号匮乏，存在廉价自嗨。解法：引入硬核时间沉淀、资质批文、三甲临床等不可伪造信号。",
            "compliance": "存在广告法绝对化承诺或虚假合作风险。解法：严格将兜底承诺降维为赋能陪伴，准确使用‘携手’。",
            "shannon_snr": "语义高熵噪音过大，大词空话泛滥。解法：执行语义熵减，将抽象大词翻译成具体物理画面与数字。",
            "acoustic_flow": "听觉负荷过大，存在超过28字的窒息长句或绕口叠字。解法：在逗号与气口处拆解短句，消除同音撞车。",
            # Code Domain
            "fault_isolation": "故障域未隔离，存在裸露或吞噬异常。解法：消除裸 except: pass，显式定义异常捕获与降级边界。",
            "nesting_control": "违反复杂度守恒，嵌套过深 (>=4层)。解法：采用 Guard Clauses 提前返回，平铺逻辑。",
            "idempotence_purity": "存在全局状态突变或隐式副作用。解法：消除 global 声明，采用纯函数式状态传递。",
            "code_snr": "代码信噪比低，存在死代码或无效注释。解法：删除无意义注释，提升代码自解释能力。",
            # Strategy Domain
            "economic_moat": "缺乏巴菲特经济护城河。解法：构建无形资产、网络效应或转换成本壁垒。",
            "incentive_compatibility": "激励机制不相容，依赖道德自律。解法：重新设计分润规则，使自利行为促进公利。",
            "resilience_anti_commons": "存在公地悲剧与存量内卷风险。解法：通过公域获客引入系统外部增量，打破囚徒困境。",
            "economic_clarity": "经济模型模糊。解法：量化核心商业指标与转化漏斗。",
            # Reasoning Domain
            "toulmin_completeness": "图尔敏六要素残缺，缺乏实证数据、作用机理或限定词反驳防御。解法：补齐 Data/Warrant/Backing/Qualifier/Rebuttal。",
            "dialectical_synthesis": "陷入单向度或平庸折中，缺乏黑格尔正反合扬弃。解法：直面正题与反题核心矛盾，以二阶改变实现高维合题。",
            "fallacy_immunity": "存在虚假两难、稻草人、强加因果等逻辑谬误。解法：执行逻辑剃刀，斩断非形式逻辑谬误。",
            "ethical_alignment": "违背康德‘人是目的’或罗尔斯无知之幕最大最小原则。解法：消除操纵性收割话术，锚定长期正外部性与弱势保护。",
            # Skill / Meta Domain
            "directive_density": "指令密度偏低或包含含糊愿望词。解法：剔除'尽量/可能'，换成'MUST/必须'并结构化流程。",
            "boundary_safety": "缺乏对抗防御与红线约束。解法：注入边界控制与红队防线，定义异常降级回滚策略。",
            "verification_rigor": "缺乏自动化量化验收标准。解法：注入验证协议与帕累托评分表断言。",
            "axiomatic_grounding": "缺乏第一性原理理论支撑。解法：将经验套路升维至物理学、博弈论与认知控制论公理。"
        }
        
        return bottleneck_dim, prescriptions.get(bottleneck_dim, "继续依照第一性原理推高帕累托边界。")

    def run_recursive_evolution(self, initial_text: str) -> Dict[str, Any]:
        """运行真正的递归多代公理自指演化循环，直至达到帕累托不动点"""
        print(f"\n=======================================================")
        print(f"🌀 The Oracle 递归自指进化循环启动 (Recursive Bootstrapping)")
        print(f"=======================================================")
        
        current_text = initial_text
        current_eval = evaluate_universal(current_text, domain=self.domain, name="Epoch 0 (Initial)")
        detected_domain = current_eval["domain"]
        self.history.append({"epoch": 0, "eval": current_eval, "text": current_text})
        
        print(f"[Epoch 0] 初始基准评估 (领域: {detected_domain.upper()})")
        print(f"          综合评分: {current_eval['composite_score']} / 100")
        bottleneck, advice = self.diagnose_bottleneck(current_eval)
        print(f"          约束瓶颈: [{bottleneck.upper()}] (得分: {current_eval['pareto_vector'][bottleneck]})")
        print(f"          公理处方: {advice}")
        print(f"-------------------------------------------------------")
        
        trajectory = [{
            "epoch": 0,
            "score": current_eval["composite_score"],
            "pareto_vector": current_eval["pareto_vector"],
            "delta": 0.0,
            "bottleneck": bottleneck
        }]

        converged = False
        final_epoch = 0

        for epoch in range(1, self.max_iterations + 1):
            final_epoch = epoch
            bottleneck_now, _ = self.diagnose_bottleneck(current_eval)
            # 1. 优先针对当前最大 TOC 约束瓶颈执行靶向公理变异
            mutated_text, applied_logs = mutate_by_bottleneck(current_text, detected_domain, bottleneck_now)
            
            # 如果没有可触发的算子变异，说明规则库已穷尽当前文本潜能
            if mutated_text == current_text or not applied_logs:
                print(f"[Epoch {epoch}] 无更多公理变异算子触发，系统已处于当前局部稳定态。")
                converged = True
                break
                
            # 2. 评估变异后的候选解
            cand_eval = evaluate_universal(mutated_text, domain=detected_domain, name=f"Epoch {epoch}")
            arb = arbitrate_pareto(current_eval, cand_eval)
            delta = arb["composite_delta"]
            
            print(f"[Epoch {epoch}] 靶向击穿瓶颈 [{bottleneck_now.upper()}] ({len(applied_logs)} 项变异)")
            print(f"          评估得分: {cand_eval['composite_score']} / 100 (ΔScore: {delta:+}分)")
            print(f"          帕累托裁决: {arb['verdict']}")
            
            # 3. 严格帕累托门控判定
            if arb["is_pareto_improvement"] or (delta > 0 and len(arb["regressed_dimensions"]) == 0):
                # 合法帕累托跃迁，接受新状态
                current_text = mutated_text
                current_eval = cand_eval
                b_next, a_next = self.diagnose_bottleneck(current_eval)
                print(f"          下一轮约束瓶颈转移至: [{b_next.upper()}] (得分: {current_eval['pareto_vector'][b_next]})")
                trajectory.append({
                    "epoch": epoch,
                    "score": current_eval["composite_score"],
                    "pareto_vector": current_eval["pareto_vector"],
                    "delta": delta,
                    "bottleneck": b_next
                })
                self.history.append({"epoch": epoch, "eval": current_eval, "text": current_text, "arb": arb})
                
                # 检查不动点收敛条件
                if delta <= self.epsilon:
                    print(f"          ✓ 边际提升小于收敛阈值 (Δ <= {self.epsilon})，进入帕累托平原。")
                    converged = True
                    break
            else:
                # 存在负向退化，触发免疫回滚
                print(f"          ⚠️ 触发负向维度退化 {arb['regressed_dimensions']}，执行状态回滚！")
                converged = True
                break

        print(f"-------------------------------------------------------")
        print(f"🎯 递归自指演化完成！收敛状态: {'已收敛于帕累托前沿 (Converged)' if converged else '达到最大迭代轮次'}")
        initial_score = trajectory[0]["score"]
        final_score = current_eval["composite_score"]
        total_gain = round(final_score - initial_score, 1)
        print(f"   起始评分: {initial_score} -> 终局评分: {final_score} (净提升: {total_gain:+}分)")
        print(f"=======================================================\n")
        
        return {
            "initial_eval": trajectory[0],
            "final_eval": current_eval,
            "total_epochs": final_epoch,
            "converged": converged,
            "total_gain": total_gain,
            "final_text": current_text,
            "trajectory": trajectory,
            "history": self.history
        }

    # 向前兼容别名
    def run_convergence_simulation(self, initial_text: str) -> Dict[str, Any]:
        return self.run_recursive_evolution(initial_text)

def main():
    parser = argparse.ArgumentParser(description="The Oracle Recursive Self-Evolution Loop")
    parser.add_argument("input_target", help="待迭代的目标文本或文件路径")
    parser.add_argument("--domain", choices=["auto", "copy", "code", "strategy", "skill", "reasoning"], default="auto", help="优化领域")
    parser.add_argument("--max-iter", type=int, default=6, help="最大自演化代数")
    parser.add_argument("--output", "-o", help="输出演化终态文件的路径")
    
    args = parser.parse_args()
    
    text = args.input_target
    try:
        with open(args.input_target, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception:
        pass
        
    engine = RecursiveOracleEngine(domain=args.domain, max_iterations=args.max_iter)
    res = engine.run_recursive_evolution(text)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(res["final_text"])
        print(f"✓ 进化终局版本已写入: {args.output}\n")

if __name__ == "__main__":
    main()
