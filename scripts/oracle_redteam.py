#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Oracle (先知) - Executable 3D Red-Teaming Adversarial Engine (三维红队对抗审讯引擎)
========================================================================================
Implements the 3 Adversarial Personas defined in `core/red-team.md`:
1. The Cynical Skeptic (极度防备的怀疑者 - 廉价自嗨、虚假动机与高熵黑话挑刺)
2. The Legal & Bug Hunter (法务与极客猎人 - 合规红线、逻辑谬误、裸异常与模糊指令挑刺)
3. The Anti-Overcorrection Arbiter (反过度修正审美官 - 白开水综合症、古德哈特堆砌作弊与窒息长句挑刺)

Zero external dependencies (Pure Python 3 Standard Library).
"""

import argparse
import json
import os
import re
import sys
from typing import Any, Dict, List

from oracle_eval import (
    COPY_CHEAP_TALK_PATTERNS,
    COPY_COSTLY_SIGNAL_PATTERNS,
    COPY_NOISE_PATTERNS,
    COPY_RED_LINE_PATTERNS,
    REASONING_FALLACY_PATTERNS,
    SKILL_AXIOMATIC_PATTERNS,
    SKILL_VAGUE_PATTERNS,
    detect_domain,
)


class RedTeamAdversary:
    def __init__(self, text: str, domain: str = "auto"):
        self.raw_text = text.strip()
        self.domain = detect_domain(self.raw_text) if domain == "auto" else domain

    def attack_as_cynical_skeptic(self) -> Dict[str, Any]:
        """角色 1：极度防备的怀疑者 (The Cynical Skeptic)"""
        attacks: List[Dict[str, str]] = []

        # 1. 扫描廉价自嗨与道德自封
        for pat in COPY_CHEAP_TALK_PATTERNS:
            m = re.findall(pat, self.raw_text)
            if m:
                attacks.append({
                    "severity": "HIGH",
                    "type": "廉价信号自嗨 (Cheap Talk)",
                    "evidence": m[0],
                    "challenge": f"老江湖冷笑：你自吹『{m[0]}』成本为零！触发 PKM 反营销雷达，必须替换为不可伪造的扎哈维昂贵信号！",
                })

        # 2. 扫描高熵公文黑话
        noise_found = []
        for pat in COPY_NOISE_PATTERNS:
            m = re.findall(pat, self.raw_text)
            if m:
                noise_found.extend(m)
        if len(noise_found) >= 2:
            attacks.append({
                "severity": "MEDIUM",
                "type": "香农高熵黑话噪音 (High-Entropy Buzzwords)",
                "evidence": ", ".join(list(set(noise_found))[:4]),
                "challenge": f"怀疑者皱眉：通篇『{noise_found[0]}』等悬浮大词，毫无具象画面感！请按费曼去术语测试降维成大白话与物理事实。",
            })

        # 3. 在文案/战略域检查昂贵信号密度
        if self.domain in ("copy", "strategy"):
            costly = [m for p in COPY_COSTLY_SIGNAL_PATTERNS for m in re.findall(p, self.raw_text)]
            numbers = re.findall(r"\d+", self.raw_text)
            if not costly and len(numbers) == 0:
                attacks.append({
                    "severity": "HIGH",
                    "type": "零昂贵信号支撑 (Zero Costly Signals)",
                    "evidence": "全文无具体数字或硬核资质背书",
                    "challenge": "怀疑者质问：没有任何时间沉淀、专利数量、医院临床或认证批文，凭什么让我相信你不是皮包公司？",
                })

        penalty = sum(20 if a["severity"] == "HIGH" else 10 for a in attacks)
        return {
            "persona": "The Cynical Skeptic (极度防备的怀疑者)",
            "score": max(10, 100 - penalty),
            "attacks_count": len(attacks),
            "attacks": attacks,
        }

    def attack_as_legal_bug_hunter(self) -> Dict[str, Any]:
        """角色 2：法务与极客猎人 (The Legal & Bug Hunter)"""
        attacks: List[Dict[str, str]] = []

        # 1. 广告法与民商法红线
        for pat, risk in COPY_RED_LINE_PATTERNS:
            m = re.findall(pat, self.raw_text)
            if m:
                attacks.append({
                    "severity": "CRITICAL",
                    "type": "法务合规红线违例 (Legal Compliance Violation)",
                    "evidence": m[0],
                    "challenge": f"法务总监警告：用词『{m[0]}』{risk}！一旦对外发布将面临行政处罚或连带民事索赔（破产吸收态）！",
                })

        # 2. 逻辑谬误扫描
        for pat, label in REASONING_FALLACY_PATTERNS:
            m = re.findall(pat, self.raw_text)
            if m:
                ev_str = m[0] if isinstance(m[0], str) else "".join(m[0])
                attacks.append({
                    "severity": "HIGH",
                    "type": f"逻辑谬误漏洞 ({label})",
                    "evidence": ev_str[:30],
                    "challenge": f"审稿极客指出：检测到『{label}』，违反图尔敏严密论证规范！",
                })

        # 3. 代码裸异常与全局突变
        if self.domain == "code":
            if re.search(r"except\s*:\s*(pass|\.\.\.)", self.raw_text) or re.search(r"except\s+Exception\s*:\s*(pass|\.\.\.)", self.raw_text):
                attacks.append({
                    "severity": "CRITICAL",
                    "type": "异常静默吞噬 (Silent Exception Swallowing)",
                    "evidence": "except: pass",
                    "challenge": "架构师警告：裸露吞噬异常违反拜占庭故障域隔离公理，会导致线上静默脏数据雪崩！",
                })
            if re.search(r"\bglobal\s+\w+", self.raw_text):
                attacks.append({
                    "severity": "HIGH",
                    "type": "非幂等全局状态污染 (Non-Idempotent Global State)",
                    "evidence": "global variable mutation",
                    "challenge": "架构师警告：使用 global 变量破坏纯函数幂等性，并发重试下必出竞态 Bug！",
                })

        # 4. 技能提示词含糊愿望词
        if self.domain == "skill":
            vagues = [m for p in SKILL_VAGUE_PATTERNS for m in re.findall(p, self.raw_text)]
            if vagues:
                attacks.append({
                    "severity": "HIGH",
                    "type": "含糊非确定性指令 (Vague Wishful Directives)",
                    "evidence": ", ".join(list(set(vagues))),
                    "challenge": f"极客猎人指出：技能规范中包含『{vagues[0]}』等弱约束词，Agent 在复杂长尾下必然发生行为漂移！",
                })

        penalty = sum(30 if a["severity"] == "CRITICAL" else (20 if a["severity"] == "HIGH" else 10) for a in attacks)
        return {
            "persona": "The Legal & Bug Hunter (法务与极客猎人)",
            "score": max(0, 100 - penalty),
            "attacks_count": len(attacks),
            "attacks": attacks,
        }

    def attack_as_anti_blandness_arbiter(self) -> Dict[str, Any]:
        """角色 3：过度修正仲裁官与反古德哈特审计员 (The Anti-Overcorrection & Anti-Goodhart Arbiter)"""
        attacks: List[Dict[str, str]] = []

        # 1. 巴德利听觉语音回路窒息句检查
        if self.domain == "copy":
            breath_units = [u.strip() for u in re.split(r"[，,、；;。！？!\?\n—]+", self.raw_text) if u.strip()]
            choking = [u for u in breath_units if len(u) > 28]
            if choking:
                attacks.append({
                    "severity": "MEDIUM",
                    "type": "巴德利听觉内存溢出 (Acoustic Breath Choking >28 chars)",
                    "evidence": choking[0][:32] + "...",
                    "challenge": f"声学导演挑刺：单口气长达 {len(choking[0])} 字无标点停顿，播音员会憋气、听众工作记忆会溢出！",
                })

            # 2. 白开水综合症检查 (Over-correction / Blandness Trap)
            char_len = len(re.sub(r"\s+", "", self.raw_text))
            numbers = re.findall(r"\d+", self.raw_text)
            vivid_markers = re.findall(r"河道|万家灯火|放大器|三甲|百强|专利|温度|底气|千家万户|时代", self.raw_text)
            if char_len > 30 and len(numbers) == 0 and len(vivid_markers) == 0:
                attacks.append({
                    "severity": "HIGH",
                    "type": "过度修正白开水综合症 (Over-Corrected Blandness Trap)",
                    "evidence": "全文缺乏具象数字、视觉隐喻与情绪峰终高潮",
                    "challenge": "美学仲裁官痛批：虽然没有违规词，但改成了温吞苍白的说明书！毫无气场与多巴胺峰值，违反帕累托反白开水铁律！",
                })

        # 3. 古德哈特关键词堆砌作弊检测 (Anti-Goodhart Keyword Stuffing Check)
        axioms = [m for p in SKILL_AXIOMATIC_PATTERNS for m in re.findall(p, self.raw_text)]
        lines = [l.strip() for l in self.raw_text.split("\n") if l.strip()]
        if len(axioms) >= 5 and len(lines) <= 3:
            attacks.append({
                "severity": "CRITICAL",
                "type": "古德哈特关键词堆砌作弊 (Goodhart Keyword Stuffing)",
                "evidence": f"仅 {len(lines)} 行文本中密集堆砌了 {len(axioms)} 个公理名词",
                "challenge": "反作弊仲裁官拦截：检测到无结构推导的公理名词堆砌（违反 Goodhart's Law #106）！拒绝虚假高分！",
            })

        penalty = sum(30 if a["severity"] == "CRITICAL" else (20 if a["severity"] == "HIGH" else 12) for a in attacks)
        return {
            "persona": "The Anti-Overcorrection & Anti-Goodhart Arbiter (反过度修正与反作弊仲裁官)",
            "score": max(0, 100 - penalty),
            "attacks_count": len(attacks),
            "attacks": attacks,
        }

    def run_full_redteam(self) -> Dict[str, Any]:
        p1 = self.attack_as_cynical_skeptic()
        p2 = self.attack_as_legal_bug_hunter()
        p3 = self.attack_as_anti_blandness_arbiter()

        all_attacks = p1["attacks"] + p2["attacks"] + p3["attacks"]
        critical_count = sum(1 for a in all_attacks if a["severity"] == "CRITICAL")
        high_count = sum(1 for a in all_attacks if a["severity"] == "HIGH")
        survival_score = round((p1["score"] * 0.35 + p2["score"] * 0.40 + p3["score"] * 0.25), 1)
        passed = (critical_count == 0) and (high_count == 0) and (survival_score >= 85.0)

        return {
            "domain": self.domain,
            "survival_score": survival_score,
            "passed_redteam": passed,
            "critical_vulnerabilities": critical_count,
            "high_vulnerabilities": high_count,
            "total_attacks_triggered": len(all_attacks),
            "personas": {
                "cynical_skeptic": p1,
                "legal_bug_hunter": p2,
                "anti_blandness_arbiter": p3,
            },
            "all_attacks": all_attacks,
        }


def print_redteam_report(rep: Dict[str, Any]) -> None:
    print("\n" + "=" * 72)
    print(f"🛡️  The Oracle 三维红队对抗审讯报告 (3D Red-Team Adversarial Audit)")
    print("=" * 72)
    status_str = "✅ 免检通过 (PASSED RED-TEAM)" if rep["passed_redteam"] else "❌ 发现致命破绽 (FAILED - NEEDS REMEDIATION)"
    print(f"📂 审计领域 (Domain)        : {rep['domain'].upper()}")
    print(f"🏆 红队生存得分 (Survival)  : {rep['survival_score']} / 100  [{status_str}]")
    print(f"⚠️  漏洞统计 (Vulnerabilities): CRITICAL={rep['critical_vulnerabilities']} | HIGH={rep['high_vulnerabilities']} | TOTAL={rep['total_attacks_triggered']}")
    print("-" * 72)
    for key, p in rep["personas"].items():
        print(f"🔥 {p['persona']} -> 得分: {p['score']}/100 ({p['attacks_count']} 处挑刺)")
        for att in p["attacks"]:
            print(f"   • [{att['severity']}] {att['type']} (证据: 『{att['evidence']}』)")
            print(f"     └─ {att['challenge']}")
    if rep["total_attacks_triggered"] == 0:
        print("✨ 三大恶魔代言人进行饱和式挑刺后，未发现任何合规、逻辑、声律或白开水漏洞！")
    print("=" * 72 + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="The Oracle - 3D Red-Team Adversarial Engine")
    parser.add_argument("target", help="Text string or file path to audit")
    parser.add_argument("--domain", choices=["auto", "copy", "code", "strategy", "skill", "reasoning"], default="auto")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if os.path.isfile(args.target):
        with open(args.target, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = args.target

    rep = RedTeamAdversary(text, domain=args.domain).run_full_redteam()
    if args.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        print_redteam_report(rep)


if __name__ == "__main__":
    main()
