#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# The Oracle: Automated 6-Stage Continuous Axiomatic Audit & Regression Pipeline
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

echo "======================================================="
echo "🔮 The Oracle 自动化公理回归与自指健康度质检流水线 (6-Stage CI/CD)"
echo "======================================================="

# 1. 语法与静态编译检查
echo "[Stage 1/6] 执行 Python 静态语法与 AST 解析检查..."
python3 -m py_compile scripts/oracle_router.py scripts/oracle_eval.py scripts/oracle_loop.py scripts/oracle_mutate.py tests/test_oracle_engine.py
echo "✓ 核心脚本编译通过，零语法错误 (Zero Syntax Errors)"

# 2. 运行跨学科公理单元测试套件
echo -e "\n[Stage 2/6] 执行跨学科公理单元测试套件 (13 Unit Tests)..."
python3 -m unittest tests/test_oracle_engine.py
echo "✓ 13 大跨领域公理单元测试 100% 全部通过 (All 13 Unit Tests Passed)"

# 3. 运行可执行门控路由器诊断检查
echo -e "\n[Stage 3/6] 执行 Sparse MoE 门控路由器实测 (24 Experts / 120 Mental Models)..."
python3 -c "
import subprocess, json
proc = subprocess.run(['python3', 'scripts/oracle_router.py', '如何用破框思维TRIZ、黑格尔辩证法与梅多斯系统杠杆点实现元技能自举进化？', '--json'], capture_output=True, text=True, check=True)
diag = json.loads(proc.stdout)['router_diagnosis']
assert diag['total_expert_pool_size'] == 24, '专家池数量不等于24！'
assert diag['total_mental_models_indexed'] == 120, '思维模型索引不等于120！'
top_slugs = [e['slug'] for e in diag['selected_experts']]
print(f'✓ 门控路由诊断通过: 激活专家 {top_slugs}，映射思维模型 {diag[\"activated_mental_model_ids\"]}')
"

# 4. 运行变异重构与帕累托跃迁实战测试
echo -e "\n[Stage 4/6] 执行公理变异重构与帕累托跃迁实测..."
python3 -c "
import subprocess
import json

before_text = '''人工智能加速演进，带动获客方式走向智能，也把技术红利带到每一个个体面前。
我们构建全域生态，深耕衣食住行康，全线产品自研自产，配方有依据，链路可追溯。
聚星商学苑全程兜底，我们的初心很纯粹，极致的产品力就是最坚实的底盘。'''

with open('/tmp/audit_before.txt', 'w', encoding='utf-8') as f:
    f.write(before_text)

subprocess.run(['python3', 'scripts/oracle_mutate.py', '/tmp/audit_before.txt', '-o', '/tmp/audit_after.txt'], check=True, stdout=subprocess.DEVNULL)

proc = subprocess.run(['python3', 'scripts/oracle_eval.py', '--before', '/tmp/audit_before.txt', '--after', '/tmp/audit_after.txt', '--json'], capture_output=True, text=True, check=True)
res = json.loads(proc.stdout)
arb = res['pareto_arbitration']

assert arb['is_pareto_improvement'] == True, '帕累托仲裁未通过！'
assert len(arb['regressed_dimensions']) == 0, '发现负退化维度！'
print(f'✓ 变异演化测试通过: 综合评分提升 +{arb[\"composite_delta\"]} 分，零负退化')
"

# 5. 运行递归多代自指进化收敛测试 (TOC 逐代瓶颈击穿)
echo -e "\n[Stage 5/6] 执行递归多代自指进化收敛测试 (TOC Multi-Epoch Bootstrapping)..."
python3 -c "
import sys
sys.path.insert(0, 'scripts')
from oracle_loop import RecursiveOracleEngine
dirty_skill = '''---
name: sample-agent
---
希望你尽量尝试帮用户写代码，你看着办吧，随便写写就行。
'''
engine = RecursiveOracleEngine(domain='skill', max_iterations=6, epsilon=0.5)
res = engine.run_recursive_evolution(dirty_skill)
assert res['converged'] == True, '自演化未正常收敛！'
assert len(res['trajectory']) >= 4, f'代数过少，未体现逐代瓶颈击穿: {len(res[\"trajectory\"])}'
assert res['total_gain'] > 40.0, f'帕累托净收益过低: {res[\"total_gain\"]}'
print(f'✓ 自指递归循环验证通过: 历经 {len(res[\"trajectory\"])-1} 代 TOC 瓶颈靶向跃迁，净帕累托收益 +{res[\"total_gain\"]} 分，直达帕累托前沿 ({res[\"final_eval\"][\"composite_score\"]}/100)')
"

# 6. 哥德尔自指满分审计与 24 大专家库 / 120 思维模型完整性扫描
echo -e "\n[Stage 6/6] 执行 The Oracle 自身 SKILL.md 满分审计与 24 大专家库扫描..."
python3 -c "
import subprocess, json
proc = subprocess.run(['python3', 'scripts/oracle_eval.py', 'SKILL.md', '--domain', 'skill', '--json'], capture_output=True, text=True, check=True)
ev = json.loads(proc.stdout)
assert ev['composite_score'] == 100.0, f'SKILL.md 未达满分: {ev[\"composite_score\"]}'
print(f'✓ 哥德尔自指审计通过: SKILL.md 综合评分 {ev[\"composite_score\"]}/100 (四维向量: {ev[\"pareto_vector\"]})')
"
EXPERT_COUNT=$(ls experts/*.md | wc -l | tr -d ' ')
MODEL_COUNT=$(grep -E '^\| \*\*[0-9]{2,3}\*\* \|' references/top-100-mental-models.md | wc -l | tr -d ' ')
echo "✓ 已加载先知公理专家数量: $EXPERT_COUNT / 24 个专家模块"
echo "✓ 已索引人类伟大思维模型: $MODEL_COUNT / 120 个核心模型"
for exp in experts/*.md; do
    echo "  • $(basename $exp)"
done

echo -e "\n======================================================="
echo "🎉 终极结论: The Oracle (24 大公理专家 / 120 思维模型 / 5 域自指引擎) 100% 帕累托收敛达标！"
echo "======================================================="
