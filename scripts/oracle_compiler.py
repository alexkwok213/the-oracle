#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Oracle (先知) v3.0 — End-to-End Axiomatic Cognitive Compiler & Self-Evolution Engine
=========================================================================================
Unifies the entire 5-Stage Cognitive Compilation Pipeline:
  Stage 1: Sparse MoE Gating Router (30 Grand Domains / 150 Mental Models)
  Stage 2: Initial 4D Pareto & Anti-Goodhart Evaluation
  Stage 3: Pre-Evolution 3D Red-Team Adversarial Attack
  Stage 4: Multi-Epoch TOC Bottleneck Recursive Evolution Loop
  Stage 5: Post-Evolution 3D Red-Team Re-Audit & Final Pareto Arbitration

Also supports `--self-audit-repo` for Gödelian repository-wide self-inspection.
Zero external dependencies (Pure Python 3 Standard Library).
"""

import argparse
import glob
import json
import os
import re
import sys
from typing import Any, Dict

from oracle_eval import arbitrate_pareto, evaluate_universal
from oracle_loop import RecursiveOracleEngine
from oracle_redteam import RedTeamAdversary
from oracle_router import EXPERT_DOMAINS, route_task


def compile_artifact(raw_text: str, domain: str = "auto", max_iter: int = 6) -> Dict[str, Any]:
    """Run the full 5-Stage Axiomatic Cognitive Compilation Pipeline on any input."""
    # Stage 1: Router
    routing = route_task(raw_text, top_k=3)["router_diagnosis"]
    detected_domain = routing["detected_category"] if domain == "auto" else domain

    # Stage 2: Initial Eval
    eval_before = evaluate_universal(raw_text, domain=detected_domain, name="Before Compilation")

    # Stage 3: Pre-Evolution Red-Team
    redteam_before = RedTeamAdversary(raw_text, domain=detected_domain).run_full_redteam()

    # Stage 4: Multi-Epoch TOC Bottleneck Evolution (suppress stdout during internal call if needed)
    engine = RecursiveOracleEngine(domain=detected_domain, max_iterations=max_iter, epsilon=0.5)
    loop_res = engine.run_recursive_evolution(raw_text)
    evolved_text = loop_res["final_text"]

    # Stage 5: Post-Evolution Eval, Red-Team & Pareto Arbitration
    eval_after = loop_res["final_eval"]
    redteam_after = RedTeamAdversary(evolved_text, domain=detected_domain).run_full_redteam()
    pareto_arb = arbitrate_pareto(eval_before, eval_after)

    return {
        "compiler_version": "3.0.0",
        "domain": detected_domain,
        "stage1_routing": routing,
        "stage2_eval_before": eval_before,
        "stage3_redteam_before": redteam_before,
        "stage4_evolution_trajectory": loop_res["trajectory"],
        "stage5_eval_after": eval_after,
        "stage5_redteam_after": redteam_after,
        "stage5_pareto_arbitration": pareto_arb,
        "compiled_output": evolved_text,
    }


def audit_oracle_repository(repo_root: str) -> Dict[str, Any]:
    """Perform a comprehensive Gödelian self-audit across the entire `the-oracle` repository."""
    expert_files = sorted(glob.glob(os.path.join(repo_root, "experts", "*.md")))
    models_file = os.path.join(repo_root, "references", "top-100-mental-models.md")
    skill_file = os.path.join(repo_root, "SKILL.md")

    with open(models_file, "r", encoding="utf-8") as f:
        models_content = f.read()
    model_rows = re.findall(r"^\| \*\*(\d{2,3})\*\* \|", models_content, re.M)

    with open(skill_file, "r", encoding="utf-8") as f:
        skill_content = f.read()

    skill_eval = evaluate_universal(skill_content, domain="skill", name="SKILL.md")
    skill_redteam = RedTeamAdversary(skill_content, domain="skill").run_full_redteam()

    # Verify every router slug maps to an actual file on disk
    missing_expert_files = []
    for exp in EXPERT_DOMAINS:
        full_p = os.path.join(repo_root, exp["file"])
        if not os.path.isfile(full_p):
            missing_expert_files.append(exp["file"])

    is_healthy = (
        len(expert_files) == 30
        and len(EXPERT_DOMAINS) == 30
        and len(model_rows) == 150
        and len(missing_expert_files) == 0
        and skill_eval["composite_score"] == 100.0
        and skill_redteam["passed_redteam"]
    )

    return {
        "repository_healthy": is_healthy,
        "experts_on_disk": len(expert_files),
        "experts_in_router": len(EXPERT_DOMAINS),
        "mental_models_indexed": len(model_rows),
        "missing_expert_files": missing_expert_files,
        "skill_md_composite_score": skill_eval["composite_score"],
        "skill_md_pareto_vector": skill_eval["pareto_vector"],
        "skill_md_redteam_survival": skill_redteam["survival_score"],
        "skill_md_redteam_passed": skill_redteam["passed_redteam"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="The Oracle v3.0 End-to-End Axiomatic Cognitive Compiler")
    parser.add_argument("target", nargs="?", help="Input text or file path to compile")
    parser.add_argument("--domain", choices=["auto", "copy", "code", "strategy", "skill", "reasoning"], default="auto")
    parser.add_argument("--max-iter", type=int, default=6, help="Max evolution epochs")
    parser.add_argument("--output", "-o", help="Write compiled output to file")
    parser.add_argument("--self-audit-repo", action="store_true", help="Run Gödelian self-audit on the-oracle repo")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    if args.self_audit_repo:
        rep = audit_oracle_repository(repo_root)
        if args.json:
            print(json.dumps(rep, ensure_ascii=False, indent=2))
        else:
            print("=" * 72)
            print("🏛️  The Oracle v3.0 哥德尔全仓自指审计证书 (Gödelian Self-Audit Certificate)")
            print("=" * 72)
            print(f"✓ 专家模块物理文件数 : {rep['experts_on_disk']} / 30")
            print(f"✓ 门控路由注册专家数 : {rep['experts_in_router']} / 30")
            print(f"✓ 人类思维模型索引数 : {rep['mental_models_indexed']} / 150")
            print(f"✓ SKILL.md 帕累托得分: {rep['skill_md_composite_score']} / 100.0 ({rep['skill_md_pareto_vector']})")
            print(f"✓ SKILL.md 红队生存率: {rep['skill_md_redteam_survival']} / 100.0 (通过: {rep['skill_md_redteam_passed']})")
            print(f"✓ 全仓自洽健康度判定 : {'100% 完美收敛 (HEALTHY)' if rep['repository_healthy'] else '存在异常 (FAILED)'}")
            print("=" * 72)
        sys.exit(0 if rep["repository_healthy"] else 1)

    if not args.target:
        parser.print_help()
        sys.exit(0)

    if os.path.isfile(args.target):
        with open(args.target, "r", encoding="utf-8") as f:
            raw_text = f.read()
    else:
        raw_text = args.target

    res = compile_artifact(raw_text, domain=args.domain, max_iter=args.max_iter)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(res["compiled_output"])

    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print("=" * 72)
        print("⚡ The Oracle v3.0 全链路认知编译汇总报告 (Cognitive Compilation Summary)")
        print("=" * 72)
        top_exps = [e["slug"] for e in res["stage1_routing"]["selected_experts"]]
        print(f"1. [门控路由] 识别域: {res['domain'].upper()} | 激活专家: {top_exps}")
        print(f"2. [帕累托跃迁] {res['stage2_eval_before']['composite_score']} -> {res['stage5_eval_after']['composite_score']} (Δ={res['stage5_pareto_arbitration']['composite_delta']:+}分 | {res['stage5_pareto_arbitration']['verdict']})")
        print(f"3. [红队抗毁度] {res['stage3_redteam_before']['survival_score']} -> {res['stage5_redteam_after']['survival_score']} / 100 (漏洞数: {res['stage3_redteam_before']['total_attacks_triggered']} -> {res['stage5_redteam_after']['total_attacks_triggered']})")
        print(f"4. [演化终局稿]:\n{res['compiled_output']}")
        print("=" * 72)


if __name__ == "__main__":
    main()
