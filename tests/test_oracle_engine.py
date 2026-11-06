#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit Test Suite for The Oracle Axiomatic Engine
Validates:
1. Shannon SNR & Noise Detection
2. Costly Signaling vs Cheap Talk
3. Compliance Red-Line Scanner
4. Acoustic Flow Breath-Unit Logic
5. Pareto Arbitrage Positive & Negative Cases
"""

import unittest
import os
import sys

# 将 scripts 目录加入 sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from oracle_eval import evaluate_universal, arbitrate_pareto, CopyEvaluator, OracleEvaluator

class TestOracleAxiomaticEngine(unittest.TestCase):

    def test_noise_detection(self):
        text_with_noise = "人工智能加速演进，带动技术红利，构建全域生态，推动持续变迁。"
        evaluator = OracleEvaluator(text_with_noise)
        res = evaluator.evaluate_noise_and_snr()
        self.assertGreater(len(res["noise_hits"]), 2)
        self.assertLess(res["snr_score"], 60)

    def test_costly_vs_cheap_talk(self):
        cheap_text = "我们的初心很纯粹，极致的产品力，良心企业，全网第一！"
        eval_cheap = OracleEvaluator(cheap_text).evaluate_signaling()
        self.assertFalse(eval_cheap["is_cheap_talk_free"])
        self.assertGreater(len(eval_cheap["cheap_talk_hits"]), 1)
        self.assertLess(eval_cheap["signaling_score"], 50)

        costly_text = "专注22年制药，拥有6大现代化生产基地，手握800多项专利，合作128家三甲医院，拿下HACCP与国家特医食品批文。"
        eval_costly = OracleEvaluator(costly_text).evaluate_signaling()
        self.assertTrue(eval_costly["is_cheap_talk_free"])
        self.assertGreaterEqual(len(eval_costly["costly_signals"]), 4)
        self.assertGreaterEqual(eval_costly["signaling_score"], 80)

    def test_compliance_red_lines(self):
        dirty_text = "我们平台全程兜底，货源你不用操心，保证稳赚不赔，并已达成战略合作协议！"
        res = OracleEvaluator(dirty_text).evaluate_compliance()
        self.assertFalse(res["is_clean"])
        self.assertGreaterEqual(len(res["violations"]), 3)
        self.assertLessEqual(res["compliance_score"], 50)

        clean_text = "聚星商学苑全程系统赋能，在货源上平台是坚实后盾，深度携手新菘福制药集团。"
        res_clean = OracleEvaluator(clean_text).evaluate_compliance()
        self.assertTrue(res_clean["is_clean"])
        self.assertEqual(res_clean["compliance_score"], 100)

    def test_acoustic_flow_choking(self):
        # 超过 28 个汉字完全没有任何标点的窒息句
        choking_text = "在这个快速变化的时代里面我们每个人都在寻找一个能够长久做下去的没有风险的确定性方向。"
        res = OracleEvaluator(choking_text).evaluate_acoustic_flow()
        self.assertGreater(res["choking_units_count"], 0)
        self.assertLess(res["acoustic_score"], 100)

        # 带有正常逗号换气气口的句子
        smooth_text = "在这个快速变化的时代，每个人都在寻找更具确定性的方向。"
        res_smooth = OracleEvaluator(smooth_smooth := smooth_text).evaluate_acoustic_flow()
        self.assertEqual(res_smooth["choking_units_count"], 0)
        self.assertEqual(res_smooth["acoustic_score"], 100)

    def test_pareto_arbitrage(self):
        # 模拟正向帕累托改进
        before = {
            "name": "B",
            "composite_score": 50,
            "pareto_vector": {"impact_signaling": 40, "compliance": 50, "shannon_snr": 40, "acoustic_flow": 70}
        }
        after_good = {
            "name": "A",
            "composite_score": 85,
            "pareto_vector": {"impact_signaling": 90, "compliance": 100, "shannon_snr": 80, "acoustic_flow": 70}
        }
        res_good = arbitrate_pareto(before, after_good)
        self.assertTrue(res_good["is_pareto_improvement"])
        self.assertEqual(len(res_good["regressed_dimensions"]), 0)

        # 模拟负向退化（拆东墙补西墙：虽然总分高了，但声律退化）
        after_regressed = {
            "name": "A_bad",
            "composite_score": 75,
            "pareto_vector": {"impact_signaling": 90, "compliance": 90, "shannon_snr": 80, "acoustic_flow": 50}
        }
        res_regressed = arbitrate_pareto(before, after_regressed)
        self.assertFalse(res_regressed["is_pareto_improvement"])
        self.assertIn("acoustic_flow", res_regressed["regressed_dimensions"])

    def test_code_domain_axioms(self):
        """测试代码领域的控制论与复杂度守恒第一性原理"""
        dirty_code = """
        def process_data(data):
            global total_count
            try:
                for a in data:
                    for b in a:
                        for c in b:
                            for d in c:
                                do_something(d)
            except:
                pass
            except Exception:
                pass
        """
        clean_code = """
        def process_data(data: list) -> list:
            results = []
            for item in flatten(data):
                try:
                    results.append(transform(item))
                except ValueError as e:
                    logger.warning("Invalid item: %s", e)
            return results
        """
        ev_dirty = evaluate_universal(dirty_code, domain="code")
        ev_clean = evaluate_universal(clean_code, domain="code")
        
        self.assertLessEqual(ev_dirty["pareto_vector"]["fault_isolation"], 60)
        self.assertEqual(ev_clean["pareto_vector"]["fault_isolation"], 100)
        
        arb = arbitrate_pareto(ev_dirty, ev_clean)
        self.assertTrue(arb["is_pareto_improvement"])
        self.assertGreater(arb["composite_delta"], 0)

    def test_strategy_domain_axioms(self):
        """测试商业战略领域的帕累托与护城河第一性原理"""
        zero_sum_strategy = "我们要在存量市场中彻底干掉对手，搞零和博弈，过度透支熟人信任，引发公地悲剧，劣币驱逐良币！"
        moat_strategy = "我们依托高门槛无形资产、专利壁垒与网络效应，构建双赢机制与激励相容分润规则，享受30%增量分成与边际成本递减，实现帕累托最优。"
        
        ev_bad = evaluate_universal(zero_sum_strategy, domain="strategy")
        ev_good = evaluate_universal(moat_strategy, domain="strategy")
        
        self.assertLess(ev_bad["composite_score"], 60)
        self.assertGreaterEqual(ev_good["composite_score"], 80)
        
        arb = arbitrate_pareto(ev_bad, ev_good)
        self.assertTrue(arb["is_pareto_improvement"])

    def test_skill_domain_axioms(self):
        """测试元技能与系统提示词架构公理"""
        vague_skill = "--- \nname: bad-prompt\n---\n希望你尽量尝试帮用户写代码，你看着办吧，随便写写就行。"
        rigorous_skill = """---
name: the-oracle
---
# 技能规范与运行时执行协议
## 阶段一：公理门控路由
必须严格执行第一性原理推导，识别香农信噪比与博弈论纳什均衡。
## 阶段二：边界控制与红队防线
严格禁止主观臆断与虚假兜底承诺。遇到异常必须执行降级与回滚协议。
## 阶段三：验证协议与帕累托验收
执行自动化测试套件断言校验，运行帕累托仲裁器，严格禁止负向退化。输出量化评分表。
"""
        ev_vague = evaluate_universal(vague_skill, domain="skill")
        ev_rigorous = evaluate_universal(rigorous_skill, domain="skill")
        
        self.assertLess(ev_vague["composite_score"], 60)
        self.assertGreaterEqual(ev_rigorous["composite_score"], 80)
        
        arb = arbitrate_pareto(ev_vague, ev_rigorous)
        self.assertTrue(arb["is_pareto_improvement"])

    def test_recursive_evolution_convergence(self):
        """测试多代递归自演化与不动点收敛"""
        from oracle_loop import RecursiveOracleEngine
        dirty_input = "我们的初心很纯粹，货源你不用操心，我们全程兜底！稳赚不赔！希望你尽量尝试一下。"
        engine = RecursiveOracleEngine(domain="copy", max_iterations=5, epsilon=0.5)
        res = engine.run_recursive_evolution(dirty_input)
        
        self.assertTrue(res["converged"])
        self.assertGreater(res["total_gain"], 15.0)
        self.assertGreaterEqual(len(res["trajectory"]), 2)

if __name__ == '__main__':
    unittest.main()
