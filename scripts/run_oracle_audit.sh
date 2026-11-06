#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# The Oracle: Automated Continuous Axiomatic Audit & Regression Pipeline
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

echo "======================================================="
echo "🔮 The Oracle 自动化公理回归与健康度质检流水线启动"
echo "======================================================="

# 1. 语法与静态编译检查
echo "[Stage 1/5] 执行 Python 静态语法与 AST 解析检查..."
python3 -m py_compile scripts/oracle_eval.py scripts/oracle_loop.py scripts/oracle_mutate.py tests/test_oracle_engine.py
echo "✓ 核心脚本编译通过，零语法错误 (Zero Syntax Errors)"

# 2. 运行跨学科公理单元测试套件
echo -e "\n[Stage 2/5] 执行跨学科公理单元测试套件 (Unit Test Suite)..."
python3 -m unittest tests/test_oracle_engine.py
echo "✓ 9 大跨领域公理单元测试 100% 全部通过 (All 9 Unit Tests Passed)"

# 3. 运行变异重构与帕累托跃迁实战测试
echo -e "\n[Stage 3/5] 执行公理变异重构与帕累托跃迁实测..."
python3 -c "
import subprocess
import json

before_text = '''人工智能加速演进，带动获客方式走向智能，也把技术红利带到每一个个体面前。
我们构建全域生态，深耕衣食住行康，全线产品自研自产，配方有依据，链路可追溯。
聚星商学苑全程兜底，我们的初心很纯粹，极致的产品力就是最坚实的底盘。'''

with open('/tmp/audit_before.txt', 'w', encoding='utf-8') as f:
    f.write(before_text)

# 调用公理变异器
subprocess.run(['python3', 'scripts/oracle_mutate.py', '/tmp/audit_before.txt', '-o', '/tmp/audit_after.txt'], check=True, stdout=subprocess.DEVNULL)

# 调用帕累托仲裁器并获取 JSON 结果
proc = subprocess.run(['python3', 'scripts/oracle_eval.py', '--before', '/tmp/audit_before.txt', '--after', '/tmp/audit_after.txt', '--json'], capture_output=True, text=True, check=True)
res = json.loads(proc.stdout)
arb = res['pareto_arbitration']

assert arb['is_pareto_improvement'] == True, '帕累托仲裁未通过！'
assert len(arb['regressed_dimensions']) == 0, '发现负退化维度！'
print(f'✓ 变异演化测试通过: 综合评分提升 +{arb[\"composite_delta\"]} 分，零负退化')
"

# 4. 运行递归多代自指进化收敛测试
echo -e "\n[Stage 4/5] 执行递归多代自指进化收敛测试 (Recursive Bootstrapping Loop)..."
python3 -c "
import sys
sys.path.insert(0, 'scripts')
from oracle_loop import RecursiveOracleEngine
dirty_skill = '''---
name: sample-agent
---
希望你尽量尝试帮用户写代码，你看着办吧，随便写写就行。
'''
engine = RecursiveOracleEngine(domain='skill', max_iterations=4, epsilon=0.5)
res = engine.run_recursive_evolution(dirty_skill)
assert res['converged'] == True, '自演化未正常收敛！'
assert res['total_gain'] > 15.0, f'帕累托净收益过低: {res[\"total_gain\"]}'
print(f'✓ 自指递归循环验证通过: 演化代数 {res[\"total_epochs\"]} 代，净帕累托收益 +{res[\"total_gain\"]} 分，收敛性确立')
"

# 5. 跨学科专家公理库覆盖完整性扫描
echo -e "\n[Stage 5/5] 执行 15 大先知专家公理库完整性与格栅扫描..."
EXPERT_COUNT=$(ls experts/*.md | wc -l | tr -d ' ')
echo "✓ 已加载先知公理专家数量: $EXPERT_COUNT 个专家模块"
for exp in experts/*.md; do
    echo "  • $(basename $exp)"
done

echo -e "\n======================================================="
echo "🎉 终极结论: The Oracle 自指自愈与帕累托健康度 100% 达标！"
echo "=======================================================\n"
