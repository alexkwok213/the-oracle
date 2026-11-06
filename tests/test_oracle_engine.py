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
from oracle_eval import OracleEvaluator, arbitrate_pareto

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

if __name__ == '__main__':
    unittest.main()
