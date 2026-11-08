#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# The Oracle v3.0: Automated 7-Stage Continuous Axiomatic Audit & Regression Pipeline
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

echo "======================================================="
echo "🔮 The Oracle v3.0 自动化公理回归与全仓自指质检流水线 (7-Stage CI/CD)"
echo "======================================================="

# 1. 语法与静态编译检查
echo "[Stage 1/7] 执行 Python 静态语法与 AST 解析检查..."
python3 -m py_compile scripts/oracle_router.py scripts/oracle_eval.py scripts/oracle_redteam.py scripts/oracle_mutate.py scripts/oracle_loop.py scripts/oracle_compiler.py tests/test_oracle_engine.py
echo "✓ 核心脚本编译通过，零语法错误 (Zero Syntax Errors)"

# 2. 运行跨学科公理单元测试套件
echo -e "\n[Stage 2/7] 执行跨学科公理单元测试套件 (16 Unit Tests)..."
python3 -m unittest tests/test_oracle_engine.py
echo "✓ 16 大跨领域公理单元测试 100% 全部通过 (All 16 Unit Tests Passed)"

# 3. 运行可执行门控路由器诊断检查 (30 Experts / 150 Models)
echo -e "\n[Stage 3/7] 执行 Sparse MoE 门控路由器实测 (30 Experts / 150 Mental Models)..."
python3 -c "
import subprocess, json
proc = subprocess.run(['python3', 'scripts/oracle_router.py', '如何用孙子兵法避实击虚、量子认识论观察者效应与科斯交易成本实现颠覆性创新？', '--json'], capture_output=True, text=True, check=True)
diag = json.loads(proc.stdout)['router_diagnosis']
assert diag['total_expert_pool_size'] == 30, f'专家池数量异常: {diag[\"total_expert_pool_size\"]}'
assert diag['total_mental_models_indexed'] == 150, f'思维模型索引异常: {diag[\"total_mental_models_indexed\"]}'
top_slugs = [e['slug'] for e in diag['selected_experts']]
print(f'✓ 门控路由诊断通过: 激活专家 {top_slugs}，映射思维模型 {diag[\"activated_mental_model_ids\"]}')
"

# 4. 运行三维红队对抗攻击实测 (3D Adversarial Engine)
echo -e "\n[Stage 4/7] 执行三维红队对抗攻击实测 (Skeptic / Bug Hunter / Anti-Blandness)..."
python3 -c "
import subprocess, json
proc = subprocess.run(['python3', 'scripts/oracle_redteam.py', '我们的初心很纯粹，保证稳赚不赔！货源你不用操心，我们全程兜底！', '--json'], capture_output=True, text=True, check=True)
rep = json.loads(proc.stdout)
assert rep['passed_redteam'] == False, '红队未拦截致命违规！'
assert rep['critical_vulnerabilities'] >= 1, '未识别出CRITICAL级别漏洞！'
print(f'✓ 三维红队攻击引擎拦截成功: 识别漏洞 {rep[\"total_attacks_triggered\"]} 处，生存分 {rep[\"survival_score\"]}/100')
"

# 5. 运行变异重构与帕累托跃迁实战测试
echo -e "\n[Stage 5/7] 执行公理变异重构与帕累托跃迁实测..."
python3 -c "
import subprocess, json

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

# 6. 运行递归多代自指进化收敛测试 (TOC 逐代瓶颈击穿)
echo -e "\n[Stage 6/7] 执行递归多代自指进化收敛测试 (TOC Multi-Epoch Bootstrapping)..."
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

# 7. 全链路编译器与哥德尔全仓自指健康度扫描
echo -e "\n[Stage 7/7] 执行 The Oracle v3.0 哥德尔全仓自指健康度审计证书..."
python3 scripts/oracle_compiler.py --self-audit-repo

echo -e "\n======================================================="
echo "🎉 终极结论: The Oracle v3.0 (30 大公理专家 / 150 思维模型 / 7 阶自指引擎) 100% 帕累托收敛达标！"
echo "======================================================="
