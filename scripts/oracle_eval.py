#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Oracle: Axiomatic Quantitative Verification Engine
Based on First Principles, Shannon SNR, Zahavi Costly Signaling, and Pareto Arbitrage.
Pure Python standard library. Zero external dependencies.
"""

import sys
import re
import json
import argparse
from typing import Dict, List, Tuple, Any

# 1. 高熵语义噪音词库 (High-Entropy Noise Lexicon)
NOISE_PATTERNS = [
    r"加速演进", r"构建全域生态", r"技术红利", r"赋能个体", r"深耕.*场景",
    r"数字化资产", r"链路可追溯", r"应时代而生", r"只为破解.*困境",
    r"打造坚实供应链", r"推动.*持续变迁", r"正气存内", r"全面涌现",
    r"我们始终坚守", r"我们的使命始终如一", r"不忘初心", r"底层逻辑",
    r"闭环", r"抓手", r"对齐", r"打法", r"心智模型"
]

# 2. 廉价信号 (Cheap Talk) 词库
CHEAP_TALK_PATTERNS = [
    r"我们的初心很纯粹", r"我们绝不割韭菜", r"我们是真心的", r"绝不坑人",
    r"良心企业", r"倾尽心血", r"不惜代价", r"极致的产品力", r"顶级品质",
    r"全网第一", r"真正为普通人", r"真诚的连接"
]

# 3. 昂贵信号 (Costly Signals) 词库（具有差异化高作伪成本）
COSTLY_SIGNAL_PATTERNS = [
    r"\d+年制药", r"\d+年科研沉淀", r"\d+大(现代化)?生产基地",
    r"\d+多?项专利", r"\d+家三甲医院", r"覆盖超?\d+家医疗机构",
    r"HACCP", r"ISO22000", r"FSSC22000", r"特医食品批文",
    r"国家市监总局.*注册", r"中国医药百强", r"柯菲平", r"临床双盲",
    r"突破\s*3\.3\s*亿", r"十万公里(的)?血管河道"
]

# 4. 合规红线高危词 (Compliance Red-Line Flags)
RED_LINE_PATTERNS = [
    (r"全程兜底", "涉嫌广告法绝对化保证/民事承诺担保"),
    (r"不用操心", "涉嫌虚假绝对担保"),
    (r"稳赚不赔", "严禁投资与创业绝对收益承诺"),
    (r"包治|根治|特效", "严禁医疗大健康绝对功效夸大"),
    (r"战略合作协议|战略伙伴", "如未签署正式盖章法务协议涉嫌虚假陈述"),
    (r"背靠某.*集团", "法律主体关系模糊且具依附低位感")
]

class OracleEvaluator:
    def __init__(self, text: str, name: str = "Candidate"):
        self.raw_text = text.strip()
        self.name = name
        self.sentences = [s.strip() for s in re.split(r'[。！？\n]+', self.raw_text) if s.strip()]
        self.char_count = len(re.sub(r'\s+', '', self.raw_text))

    def evaluate_noise_and_snr(self) -> Dict[str, Any]:
        """香农信息论维度：计算语义熵与高信噪比"""
        noise_hits = []
        for p in NOISE_PATTERNS:
            matches = re.findall(p, self.raw_text)
            if matches:
                noise_hits.extend(matches)
        
        # 统计高信息密度要素（具体数字、单位、硬核实体）
        concrete_facts = re.findall(r'\d+[\u4e00-\u9fa5a-zA-Z%]+', self.raw_text)
        
        noise_penalty = min(len(noise_hits) * 8, 60)
        fact_bonus = min(len(concrete_facts) * 6, 40)
        
        snr_score = max(10, min(100, 70 - noise_penalty + fact_bonus))
        
        return {
            "snr_score": snr_score,
            "noise_hits": noise_hits,
            "concrete_facts_count": len(concrete_facts),
            "fact_samples": concrete_facts[:5]
        }

    def evaluate_signaling(self) -> Dict[str, Any]:
        """博弈论维度：扎哈维昂贵信号 vs 廉价信号 (Cheap Talk)"""
        costly_hits = []
        for p in COSTLY_SIGNAL_PATTERNS:
            matches = re.findall(p, self.raw_text)
            if matches:
                costly_hits.extend(matches)
                
        cheap_hits = []
        for p in CHEAP_TALK_PATTERNS:
            matches = re.findall(p, self.raw_text)
            if matches:
                cheap_hits.extend(matches)
                
        # 昂贵信号加分，廉价信号重罚
        base_score = 50
        score = base_score + (len(costly_hits) * 10) - (len(cheap_hits) * 15)
        signaling_score = max(0, min(100, score))
        
        return {
            "signaling_score": signaling_score,
            "costly_signals": list(set(costly_hits)),
            "cheap_talk_hits": list(set(cheap_hits)),
            "is_cheap_talk_free": len(cheap_hits) == 0
        }

    def evaluate_compliance(self) -> Dict[str, Any]:
        """法务红线维度：广告法与民事责任风险扫描"""
        violations = []
        for p, reason in RED_LINE_PATTERNS:
            matches = re.findall(p, self.raw_text)
            if matches:
                violations.append({
                    "pattern": p,
                    "matched": list(set(matches)),
                    "risk": reason
                })
                
        compliance_score = max(0, 100 - len(violations) * 25)
        
        return {
            "compliance_score": compliance_score,
            "is_clean": len(violations) == 0,
            "violations": violations
        }

    def evaluate_acoustic_flow(self) -> Dict[str, Any]:
        """认知生理维度：听觉负荷与语音回路顺畅度（基于换气单元 Breath Units）"""
        # 1. 最小换气单元（任何标点或换行都提供气口）
        breath_units = [u.strip() for u in re.split(r'[，,、；;。！？!\?\n—]+', self.raw_text) if u.strip()]
        
        # 窒息句检测：连续超过 28 个汉字没有任何停顿气口
        choking_units = [u for u in breath_units if len(u) > 28]
        
        # 2. 绕口叠字检测（相隔4字以内的同字重复，排除正常词汇叠音）
        stutters = []
        for s in self.sentences:
            for i in range(len(s) - 3):
                if s[i] == s[i+2] and s[i] in "一人做其这":
                    stutters.append(s[i:i+3])
        
        penalty = len(choking_units) * 15 + len(stutters) * 10
        acoustic_score = max(20, min(100, 100 - penalty))
        
        return {
            "acoustic_score": acoustic_score,
            "total_breath_units": len(breath_units),
            "choking_units_count": len(choking_units),
            "choking_samples": choking_units[:3],
            "stutters": list(set(stutters))
        }

    def run_full_evaluation(self) -> Dict[str, Any]:
        snr = self.evaluate_noise_and_snr()
        sig = self.evaluate_signaling()
        comp = self.evaluate_compliance()
        aco = self.evaluate_acoustic_flow()
        
        # 综合四维帕累托向量 (4D Pareto Vector)
        # [Impact/Signaling, Compliance, SNR, AcousticFlow]
        v_impact = sig["signaling_score"]
        v_comp = comp["compliance_score"]
        v_snr = snr["snr_score"]
        v_aco = aco["acoustic_score"]
        
        composite_score = round((v_impact * 0.3) + (v_comp * 0.3) + (v_snr * 0.2) + (v_aco * 0.2), 1)
        
        return {
            "name": self.name,
            "char_count": self.char_count,
            "composite_score": composite_score,
            "pareto_vector": {
                "impact_signaling": v_impact,
                "compliance": v_comp,
                "shannon_snr": v_snr,
                "acoustic_flow": v_aco
            },
            "details": {
                "snr": snr,
                "signaling": sig,
                "compliance": comp,
                "acoustic": aco
            }
        }

def arbitrate_pareto(before_res: Dict[str, Any], after_res: Dict[str, Any]) -> Dict[str, Any]:
    """帕累托仲裁器：严格判断是否属于无副作用的帕累托改进"""
    v_b = before_res["pareto_vector"]
    v_a = after_res["pareto_vector"]
    
    deltas = {k: v_a[k] - v_b[k] for k in v_b}
    
    has_negative_drift = any(d < 0 for d in deltas.values())
    has_positive_gain = any(d > 0 for d in deltas.values())
    
    is_pareto_improvement = (not has_negative_drift) and has_positive_gain
    
    regressed_dimensions = [k for k, d in deltas.items() if d < 0]
    improved_dimensions = [k for k, d in deltas.items() if d > 0]
    
    return {
        "is_pareto_improvement": is_pareto_improvement,
        "deltas": deltas,
        "composite_delta": round(after_res["composite_score"] - before_res["composite_score"], 1),
        "improved_dimensions": improved_dimensions,
        "regressed_dimensions": regressed_dimensions,
        "verdict": "合法帕累托跃迁 (Valid Pareto Shift)" if is_pareto_improvement else "非帕累托负优化 (Zero-Sum Degradation)"
    }

def print_report(res: Dict[str, Any]):
    print(f"\n=======================================================")
    print(f"🔮 The Oracle 评估报告: [{res['name']}] (字数: {res['char_count']})")
    print(f"-------------------------------------------------------")
    print(f"综合评分 (Composite Score): {res['composite_score']} / 100")
    print(f"四维帕累托向量 (4D Pareto Vector):")
    v = res["pareto_vector"]
    print(f"  • [昂贵信号/影响力] Impact/Signaling : {v['impact_signaling']}/100")
    print(f"  • [合规与真实度] Compliance       : {v['compliance']}/100")
    print(f"  • [香农信噪比] Shannon SNR       : {v['shannon_snr']}/100")
    print(f"  • [声律呼吸感] Acoustic Flow     : {v['acoustic_flow']}/100")
    print(f"-------------------------------------------------------")
    d = res["details"]
    if d["compliance"]["violations"]:
        print("⚠️ 发现合规红线违规项:")
        for viol in d["compliance"]["violations"]:
            print(f"   - {viol['matched']}: {viol['risk']}")
    else:
        print("✓ 合规红线扫描通过 (Zero Red-Line Flags)")
        
    if d["signaling"]["cheap_talk_hits"]:
        print(f"⚠️ 发现廉价信号 (Cheap Talk): {d['signaling']['cheap_talk_hits']}")
    else:
        print("✓ 零廉价自白自嗨 (Zero Cheap Talk)")
        
    print(f"✓ 昂贵信号实体数量: {len(d['signaling']['costly_signals'])} 个")
    print(f"✓ 高熵噪音匹配项: {len(d['snr']['noise_hits'])} 处")
    print(f"=======================================================\n")

def main():
    parser = argparse.ArgumentParser(description="The Oracle Axiomatic Evaluator")
    parser.add_argument("input_text", nargs="?", help="待评估文本或文件路径")
    parser.add_argument("--before", help="优化前文本或文件路径")
    parser.add_argument("--after", help="优化后文本或文件路径")
    parser.add_argument("--json", action="store_true", help="输出结构化 JSON 数据")
    
    args = parser.parse_args()
    
    if args.before and args.after:
        with open(args.before, 'r', encoding='utf-8') as f:
            t_b = f.read()
        with open(args.after, 'r', encoding='utf-8') as f:
            t_a = f.read()
            
        ev_b = OracleEvaluator(t_b, name="优化前 (Before)").run_full_evaluation()
        ev_a = OracleEvaluator(t_a, name="优化后 (After)").run_full_evaluation()
        arb = arbitrate_pareto(ev_b, ev_a)
        
        if args.json:
            print(json.dumps({"before": ev_b, "after": ev_a, "pareto_arbitration": arb}, ensure_ascii=False, indent=2))
        else:
            print_report(ev_b)
            print_report(ev_a)
            print(f"⚖️ 帕累托仲裁决议 (Pareto Arbitration Verdict):")
            print(f"   结论: {arb['verdict']}")
            print(f"   综合提升: {arb['composite_delta']} 分")
            print(f"   正向改进维度: {arb['improved_dimensions']}")
            if arb['regressed_dimensions']:
                print(f"   ❌ 负向退化维度: {arb['regressed_dimensions']}")
            print(f"=======================================================\n")
    elif args.input_text:
        text = args.input_text
        try:
            with open(args.input_text, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception:
            pass
            
        ev = OracleEvaluator(text).run_full_evaluation()
        if args.json:
            print(json.dumps(ev, ensure_ascii=False, indent=2))
        else:
            print_report(ev)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
