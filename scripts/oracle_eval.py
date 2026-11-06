#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Oracle: Universal Multi-Domain Axiomatic Verification Engine
Powered by First Principles:
- Copy Domain: Zahavi Costly Signaling, Shannon SNR, PKM, Acoustic Breath Units
- Code Domain: Tesler Complexity Conservation, Shannon Code Entropy, Fault Domain Isolation, Idempotence
- Strategy Domain: Pareto Frontier, Economic Moats, Incentive Compatibility, Gause Niche Differentiation
Pure Python standard library. Zero external dependencies.
"""

import sys
import re
import ast
import json
import argparse
from typing import Dict, List, Tuple, Any

# ==========================================
# 1. 商业文案领域公理规则库 (Copy Domain)
# ==========================================
COPY_NOISE_PATTERNS = [
    r"加速演进", r"构建全域生态", r"技术红利", r"赋能个体", r"深耕.*场景",
    r"数字化资产", r"链路可追溯", r"应时代而生", r"只为破解.*困境",
    r"打造坚实供应链", r"推动.*持续变迁", r"正气存内", r"全面涌现",
    r"我们始终坚守", r"我们的使命始终如一", r"不忘初心", r"底层逻辑",
    r"闭环", r"抓手", r"对齐", r"打法", r"心智模型"
]

COPY_CHEAP_TALK_PATTERNS = [
    r"我们的初心很纯粹", r"我们绝不割韭菜", r"我们是真心的", r"绝不坑人",
    r"良心企业", r"倾尽心血", r"不惜代价", r"极致的产品力", r"顶级品质",
    r"全网第一", r"真正为普通人", r"真诚的连接"
]

COPY_COSTLY_SIGNAL_PATTERNS = [
    r"\d+年制药", r"\d+年科研沉淀", r"\d+大(现代化)?生产基地",
    r"\d+多?项专利", r"\d+家三甲医院", r"覆盖超?\d+家医疗机构",
    r"HACCP", r"ISO22000", r"FSSC22000", r"特医食品批文",
    r"国家市监总局.*注册", r"中国医药百强", r"柯菲平", r"临床双盲",
    r"突破\s*3\.3\s*亿", r"十万公里(的)?血管河道"
]

COPY_RED_LINE_PATTERNS = [
    (r"全程兜底", "涉嫌广告法绝对化保证/民事承诺担保"),
    (r"不用操心", "涉嫌虚假绝对担保"),
    (r"稳赚不赔", "严禁投资与创业绝对收益承诺"),
    (r"包治|根治|特效", "严禁医疗大健康绝对功效夸大"),
    (r"战略合作协议|战略伙伴", "如未签署正式盖章法务协议涉嫌虚假陈述"),
    (r"背靠某.*集团", "法律主体关系模糊且具依附低位感")
]

class CopyEvaluator:
    def __init__(self, text: str, name: str = "Candidate"):
        self.raw_text = text.strip()
        self.name = name
        self.char_count = len(re.sub(r'\s+', '', self.raw_text))

    def evaluate_noise_and_snr(self) -> Dict[str, Any]:
        noise_hits = []
        for p in COPY_NOISE_PATTERNS:
            matches = re.findall(p, self.raw_text)
            if matches: noise_hits.extend(matches)
        concrete_facts = re.findall(r'\d+[\u4e00-\u9fa5a-zA-Z%]+', self.raw_text)
        snr_score = max(10, min(100, 70 - min(len(noise_hits)*8, 60) + min(len(concrete_facts)*6, 40)))
        return {"snr_score": snr_score, "noise_hits": noise_hits, "concrete_facts_count": len(concrete_facts)}

    def evaluate_signaling(self) -> Dict[str, Any]:
        costly_hits = []
        for p in COPY_COSTLY_SIGNAL_PATTERNS:
            m = re.findall(p, self.raw_text)
            if m: costly_hits.extend(m)
        cheap_hits = []
        for p in COPY_CHEAP_TALK_PATTERNS:
            m = re.findall(p, self.raw_text)
            if m: cheap_hits.extend(m)
        sig_score = max(0, min(100, 50 + len(costly_hits)*10 - len(cheap_hits)*15))
        return {"signaling_score": sig_score, "costly_signals": list(set(costly_hits)), "cheap_talk_hits": list(set(cheap_hits)), "is_cheap_talk_free": len(cheap_hits) == 0}

    def evaluate_compliance(self) -> Dict[str, Any]:
        violations = []
        for p, r in COPY_RED_LINE_PATTERNS:
            m = re.findall(p, self.raw_text)
            if m: violations.append({"pattern": p, "matched": list(set(m)), "risk": r})
        comp_score = max(0, 100 - len(violations)*25)
        return {"compliance_score": comp_score, "is_clean": len(violations) == 0, "violations": violations}

    def evaluate_acoustic_flow(self) -> Dict[str, Any]:
        breath_units = [u.strip() for u in re.split(r'[，,、；;。！？!\?\n—]+', self.raw_text) if u.strip()]
        choking_units = [u for u in breath_units if len(u) > 28]
        sentences = [s.strip() for s in re.split(r'[。！？\n]+', self.raw_text) if s.strip()]
        stutters = []
        for s in sentences:
            for i in range(len(s) - 3):
                if s[i] == s[i+2] and s[i] in "一人做其这":
                    stutters.append(s[i:i+3])
        aco_score = max(20, min(100, 100 - len(choking_units)*15 - len(stutters)*10))
        return {"acoustic_score": aco_score, "choking_units_count": len(choking_units), "stutters": list(set(stutters))}

    def evaluate(self) -> Dict[str, Any]:
        snr = self.evaluate_noise_and_snr()
        sig = self.evaluate_signaling()
        comp = self.evaluate_compliance()
        aco = self.evaluate_acoustic_flow()
        v = {
            "impact_signaling": sig["signaling_score"],
            "compliance": comp["compliance_score"],
            "shannon_snr": snr["snr_score"],
            "acoustic_flow": aco["acoustic_score"]
        }
        composite = round(v["impact_signaling"]*0.3 + v["compliance"]*0.3 + v["shannon_snr"]*0.2 + v["acoustic_flow"]*0.2, 1)
        return {
            "domain": "copy",
            "name": self.name,
            "char_count": self.char_count,
            "composite_score": composite,
            "pareto_vector": v,
            "details": {
                "snr": snr,
                "signaling": sig,
                "compliance": comp,
                "acoustic": aco,
                "violations": comp["violations"],
                "cheap_talk_hits": sig["cheap_talk_hits"],
                "costly_signals": sig["costly_signals"],
                "noise_hits": snr["noise_hits"]
            }
        }

# 向前兼容别名
OracleEvaluator = CopyEvaluator

# ==========================================
# 2. 软件代码与系统架构领域公理 (Code Domain)
# ==========================================
class CodeEvaluator:
    def __init__(self, code: str):
        self.code = code.strip()

    def evaluate(self) -> Dict[str, Any]:
        """基于物理控制论第一性原理评估代码质量"""
        lines = [l for l in self.code.split('\n') if l.strip()]
        total_lines = len(lines)
        
        # 1. 故障域隔离 (Fault Domain Isolation) & 异常吞噬检测
        bare_excepts = re.findall(r'except\s*:\s*(pass|\.\.\.)', self.code)
        catch_all = re.findall(r'except\s+Exception\s*:\s*(pass|\.\.\.)', self.code)
        fault_penalty = (len(bare_excepts) + len(catch_all)) * 25
        fault_score = max(10, 100 - fault_penalty)

        # 2. 复杂度守恒与深层嵌套 (Deep Nesting - Tesler's Law)
        deep_nesting = 0
        for l in lines:
            indent = len(l) - len(l.lstrip())
            if indent >= 16: # 4级以上缩进
                deep_nesting += 1
        nesting_score = max(20, 100 - min(deep_nesting * 5, 80))

        # 3. 幂等性与状态纯度 (Idempotence & Mutation)
        global_mutations = re.findall(r'\bglobal\s+\w+', self.code)
        side_effect_penalty = len(global_mutations) * 20
        idempotence_score = max(20, 100 - side_effect_penalty)

        # 4. 香农代码信噪比 (Shannon Code SNR: 有效代码 vs 冗余死代码/注释)
        comment_lines = len([l for l in lines if l.strip().startswith('#') or l.strip().startswith('//')])
        ratio = (total_lines - comment_lines) / max(total_lines, 1)
        snr_score = round(min(100, max(30, ratio * 100)))

        # Python AST 深度解析（如果是合法的 Python）
        ast_valid = False
        try:
            tree = ast.parse(self.code)
            ast_valid = True
        except SyntaxError:
            pass

        v = {
            "fault_isolation": fault_score,
            "nesting_control": nesting_score,
            "idempotence_purity": idempotence_score,
            "code_snr": snr_score
        }
        composite = round(v["fault_isolation"]*0.35 + v["nesting_control"]*0.25 + v["idempotence_purity"]*0.2 + v["code_snr"]*0.2, 1)

        return {
            "domain": "code",
            "lines_count": total_lines,
            "is_ast_valid": ast_valid,
            "composite_score": composite,
            "pareto_vector": v,
            "details": {
                "bare_except_count": len(bare_excepts),
                "catch_all_pass_count": len(catch_all),
                "deep_nesting_lines": deep_nesting,
                "global_mutations": global_mutations
            }
        }

# ==========================================
# 3. 商业模式与战略机制领域公理 (Strategy Domain)
# ==========================================
STRATEGY_MOAT_PATTERNS = [
    r"网络效应", r"转换成本", r"高门槛无形资产", r"特许专营", r"规模经济",
    r"排他性合作", r"成本领先", r"专利壁垒", r"数据飞轮"
]
STRATEGY_INCENTIVE_PATTERNS = [
    r"激励相容", r"利益一致性", r"帕累托最优", r"动态博弈", r"纳什均衡",
    r"边际成本递减", r"增量分成", r"双赢机制"
]
STRATEGY_COMMONS_TRAGEDY_PATTERNS = [
    r"零和博弈", r"存量内卷", r"公地悲剧", r"过度透支", r"劣币驱逐良币"
]

class StrategyEvaluator:
    def __init__(self, text: str):
        self.text = text.strip()

    def evaluate(self) -> Dict[str, Any]:
        """基于微观经济学与博弈论评估商业战略与机制设计"""
        moats = []
        for p in STRATEGY_MOAT_PATTERNS:
            m = re.findall(p, self.text)
            if m: moats.extend(m)
            
        incentives = []
        for p in STRATEGY_INCENTIVE_PATTERNS:
            m = re.findall(p, self.text)
            if m: incentives.extend(m)
            
        risks = []
        for p in STRATEGY_COMMONS_TRAGEDY_PATTERNS:
            m = re.findall(p, self.text)
            if m: risks.extend(m)

        moat_score = min(100, max(20, len(moats) * 20))
        incentive_score = min(100, max(20, len(incentives) * 20))
        resilience_score = max(20, 100 - len(risks) * 20)
        clarity_score = min(100, max(30, 60 + len(re.findall(r'\d+%', self.text))*10))

        v = {
            "economic_moat": moat_score,
            "incentive_compatibility": incentive_score,
            "resilience_anti_commons": resilience_score,
            "economic_clarity": clarity_score
        }
        composite = round(v["economic_moat"]*0.3 + v["incentive_compatibility"]*0.3 + v["resilience_anti_commons"]*0.2 + v["economic_clarity"]*0.2, 1)

        return {
            "domain": "strategy",
            "composite_score": composite,
            "pareto_vector": v,
            "details": {
                "identified_moats": list(set(moats)),
                "incentive_mechanisms": list(set(incentives)),
                "identified_systemic_risks": list(set(risks))
            }
        }

# ==========================================
# 4. 全局自动域检测与统一仲裁器
# ==========================================
def detect_domain(text: str) -> str:
    """自动判断输入是代码、文案还是商业战略"""
    code_indicators = [r'def\s+\w+\(', r'class\s+\w+[:\(]', r'import\s+\w+', r'function\s*\(', r'const\s+\w+\s*=']
    if any(re.search(p, text) for p in code_indicators):
        return "code"
    strategy_indicators = [r'商业模式', r'机制设计', r'分润', r'代币经济', r'飞轮', r'生态位', r'纳什均衡']
    if len([p for p in strategy_indicators if re.search(p, text)]) >= 2:
        return "strategy"
    return "copy"

def arbitrate_pareto(before_res: Dict[str, Any], after_res: Dict[str, Any]) -> Dict[str, Any]:
    """跨领域通用帕累托仲裁器：数学化判定向量是否严格单调不减"""
    v_b = before_res["pareto_vector"]
    v_a = after_res["pareto_vector"]
    
    # 对齐共同维度
    common_keys = [k for k in v_b if k in v_a]
    deltas = {k: v_a[k] - v_b[k] for k in common_keys}
    
    has_negative_drift = any(d < 0 for d in deltas.values())
    has_positive_gain = any(d > 0 for d in deltas.values())
    
    is_pareto = (not has_negative_drift) and has_positive_gain
    
    return {
        "is_pareto_improvement": is_pareto,
        "domain": after_res.get("domain", "universal"),
        "deltas": deltas,
        "composite_delta": round(after_res["composite_score"] - before_res["composite_score"], 1),
        "improved_dimensions": [k for k, d in deltas.items() if d > 0],
        "regressed_dimensions": [k for k, d in deltas.items() if d < 0],
        "verdict": "合法帕累托跃迁 (Valid Pareto Shift)" if is_pareto else "非帕累托负优化 (Zero-Sum Degradation)"
    }

def evaluate_universal(text: str, domain: str = "auto", name: str = "Candidate") -> Dict[str, Any]:
    if domain == "auto":
        domain = detect_domain(text)
        
    if domain == "code":
        res = CodeEvaluator(text).evaluate()
    elif domain == "strategy":
        res = StrategyEvaluator(text).evaluate()
    else:
        res = CopyEvaluator(text).evaluate()
        
    res["name"] = name
    return res

def print_universal_report(res: Dict[str, Any]):
    print(f"\n=======================================================")
    print(f"🔮 The Oracle 评估报告: [{res['name']}] (领域: {res['domain'].upper()})")
    print(f"-------------------------------------------------------")
    print(f"综合评分 (Composite Score): {res['composite_score']} / 100")
    print(f"四维帕累托向量 (4D Pareto Vector):")
    for k, score in res["pareto_vector"].items():
        print(f"  • {k.replace('_', ' ').title():<25}: {score}/100")
    print(f"-------------------------------------------------------")
    d = res.get("details", {})
    if res["domain"] == "code":
        print(f"✓ AST 语法合法性: {res.get('is_ast_valid')}")
        print(f"✓ 裸露/吞噬异常 (Bare/Catch-All Except): {d.get('bare_except_count') + d.get('catch_all_pass_count')} 处")
        print(f"✓ 深层嵌套行数 (Deep Nesting >= 4层): {d.get('deep_nesting_lines')} 行")
        print(f"✓ 全局状态副作用 (Global Mutations): {len(d.get('global_mutations'))} 处")
    elif res["domain"] == "copy":
        if d.get("violations"):
            print("⚠️ 发现合规红线违规项:")
            for viol in d["violations"]:
                print(f"   - {viol['matched']}: {viol['risk']}")
        else:
            print("✓ 合规红线扫描通过 (Zero Red-Line Flags)")
        if d.get("cheap_talk_hits"):
            print(f"⚠️ 发现廉价信号 (Cheap Talk): {d['cheap_talk_hits']}")
        else:
            print("✓ 零廉价自白自嗨 (Zero Cheap Talk)")
        print(f"✓ 昂贵信号实体数量: {len(d.get('costly_signals', []))} 个")
        print(f"✓ 高熵噪音匹配项: {len(d.get('noise_hits', []))} 处")
    elif res["domain"] == "strategy":
        print(f"✓ 识别出的核心护城河: {d.get('identified_moats')}")
        print(f"✓ 激励相容机制设计: {d.get('incentive_mechanisms')}")
        print(f"✓ 公地悲剧/系统性风险: {d.get('identified_systemic_risks')}")
    print(f"=======================================================\n")

def main():
    parser = argparse.ArgumentParser(description="The Oracle Universal Axiomatic Evaluator")
    parser.add_argument("input_text", nargs="?", help="待评估文本或文件路径")
    parser.add_argument("--domain", choices=["auto", "copy", "code", "strategy"], default="auto", help="评估领域")
    parser.add_argument("--before", help="优化前文本或文件路径")
    parser.add_argument("--after", help="优化后文本或文件路径")
    parser.add_argument("--json", action="store_true", help="输出结构化 JSON 数据")
    
    args = parser.parse_args()
    
    if args.before and args.after:
        with open(args.before, 'r', encoding='utf-8') as f:
            t_b = f.read()
        with open(args.after, 'r', encoding='utf-8') as f:
            t_a = f.read()
            
        ev_b = evaluate_universal(t_b, domain=args.domain, name="优化前 (Before)")
        ev_a = evaluate_universal(t_a, domain=args.domain, name="优化后 (After)")
        arb = arbitrate_pareto(ev_b, ev_a)
        
        if args.json:
            print(json.dumps({"before": ev_b, "after": ev_a, "pareto_arbitration": arb}, ensure_ascii=False, indent=2))
        else:
            print_universal_report(ev_b)
            print_universal_report(ev_a)
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
            
        ev = evaluate_universal(text, domain=args.domain)
        if args.json:
            print(json.dumps(ev, ensure_ascii=False, indent=2))
        else:
            print_universal_report(ev)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
