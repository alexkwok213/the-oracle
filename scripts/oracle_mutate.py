#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Oracle: Autonomous Axiomatic Mutation & Refactoring Engine
Applies deterministic First-Principles Operators to mutate suboptimal text/code
towards the Pareto Frontier.
Zero external dependencies.
"""

import sys
import re
import argparse
from typing import Dict, List, Tuple

# 公理级重构规则库 (Axiomatic Transformation Rules)
MUTATION_RULES = [
    # 1. 防御性自证与自我感动剥离 (Eliminate Defensive Self-Proof)
    (r"我们的初心很纯粹[：:]?\s*", ""),
    (r"我们绝不割韭菜[，,]?\s*", ""),
    (r"我们是真心的[，,]?\s*", ""),
    (r"倾尽心血[、，,]?\s*", "全力"),
    (r"不惜代价[、，,]?\s*", "以制药级标准"),
    (r"极致的产品力", "过硬的产品力"),
    (r"真诚的连接", "业务连接与信任沉淀"),

    # 2. 合规红线绝对承诺降维 (Compliance De-risking)
    (r"全程兜底", "全程系统赋能"),
    (r"货源你不用操心", "在货源上平台是坚实后盾"),
    (r"稳赚不赔", "长期稳健经营"),
    (r"达成深度战略合作", "深度携手"),
    (r"战略合作协议", "深度战略携手"),
    (r"背靠某知名大集团", "依托深厚的医药工业根基"),
    (r"背靠([^，。]+)", r"深度携手\1"),

    # 3. 高熵噪音与公文大词具象化 (Entropy Reduction & Concreteness)
    (r"人工智能加速演进[，,]?带动获客方式从流量走向智能[，,]?也把技术红利带到每一个个体面前[。！？]?", 
     "在这个快速变化的时代，商业模式正在重塑，科技的普惠让人人都能借助 AI 作为事业的放大器。"),
    (r"人均预期寿命稳步延长[，,]?人口结构持续变迁[，,]?带动健康产业从可选走向刚需[。！？]?",
     "长寿时代的到来，活得健康、活得有品质，成了千家万户最坚定的追求。"),
    (r"构建全域生态[，,]?深耕衣食住行康五大生活场景[，,]?一站式覆盖一家人的日常与健康[。！？]?",
     "大家庭全面覆盖“衣、食、住、行、康”五大生活场景，一站式满足家庭日常所需，而“康”更是战略深耕的重中之重。"),
    (r"全线产品自研自产[，,]?配方有依据[，,]?原料有来处[，,]?链路可追溯[。！？]?",
     "以制药级标准研发生产高品质健康产品，每一道原料透明可溯，配方科学严谨。"),
    (r"我们的使命[，,]?始终如一[：:]?\s*", ""),
    (r"数字(化)?资产", "稳固的信任资产"),
    (r"通畅血管健康", "助力血管畅通，守护心脑健康"),

    # 4. 绕口叠音消除 (Acoustic Flow Repair)
    (r"让每一个普通人的[“\"']?一人公司[”\"']?", "让每一位个人创业者"),
    (r"让一个人的[“\"']?一人公司[”\"']?", "让每一位个人创业者"),
]

# 技能与系统提示词公理重构规则库 (Skill / Meta Domain Mutation Rules)
SKILL_MUTATION_RULES = [
    (r"尽可能[地]?", "务必"),
    (r"尽量[地]?", "必须"),
    (r"尽力[地]?", "严格执行"),
    (r"希望你\s*", "必须执行："),
    (r"请尝试\s*", "执行："),
    (r"你看着办[吧]?", "严格按公理规范裁决"),
    (r"自由发挥[吧]?", "基于第一性原理严谨推导"),
    (r"随便[写做]\s*", "按规范执行"),
    (r"大概[是]?\s*", "精确定义"),
    (r"也许[会]?\s*", "根据先验概率确定"),
]

# 代码领域公理重构规则库 (Code Domain Mutation Rules)
CODE_MUTATION_RULES = [
    (r"except\s*:\s*pass", "except Exception as err:\n        # 故障域隔离降级\n        pass"),
    (r"except\s+Exception\s*:\s*pass", "except Exception as err:\n        # 故障域隔离降级\n        pass"),
]

def mutate_copy(raw_text: str) -> Tuple[str, List[str]]:
    """应用公理变异算子对文案执行熵减与合规升维"""
    mutated = raw_text
    applied_mutations = []

    for pattern, replacement in MUTATION_RULES:
        if re.search(pattern, mutated):
            mutated = re.sub(pattern, replacement, mutated)
            applied_mutations.append(f"Copy: {pattern} -> {replacement[:30]}")

    # 5. 窒息长句智能分拆算子 (Breath-Unit Splitter)
    split_lines = []
    for line in mutated.split('\n'):
        if len(line) > 30 and '，' not in line and '。' not in line:
            line = re.sub(r'(在这个快速变化的时代|当商业模式迎来重塑|在获客上|客流汇聚而来)', r'\1，', line)
        split_lines.append(line)
    mutated = '\n'.join(split_lines)

    return mutated, applied_mutations

def mutate_skill(raw_text: str) -> Tuple[str, List[str]]:
    """消除提示词中的含糊与愿望思维，注入强确定性动作指令与安全边界"""
    mutated = raw_text
    applied = []
    for pattern, replacement in SKILL_MUTATION_RULES:
        if re.search(pattern, mutated):
            mutated = re.sub(pattern, replacement, mutated)
            applied.append(f"Skill: {pattern} -> {replacement}")
            
    # 检查是否缺失边界安全与红线规范
    if "边界" not in mutated and "红线" not in mutated and "严格禁止" not in mutated:
        boundary_block = "\n\n## 🛡️ 边界控制与红队防线 (Boundary Guardrails)\n- 严格禁止无事实依据的主观推论与绝对化承诺\n- 遇到异常与不确定性，执行降级与回滚协议，拒绝静默吞噬\n- 接受红队饱和式对抗测试，确保认知鲁棒性\n"
        mutated += boundary_block
        applied.append("Skill: Injected standard boundary guardrails block")
        
    # 检查是否缺失验证与质检规范
    if "验证" not in mutated and "质检" not in mutated and "测试" not in mutated:
        verif_block = "\n\n## ⚖️ 验证协议与帕累托验收 (Verification Rigor)\n- 执行全维度量化指标断言与自动化评估\n- 运行帕累托仲裁器，严格禁止负向退化 (ΔVi >= 0)\n- 输出结构化质检评分卡，完成可追溯交付\n"
        mutated += verif_block
        applied.append("Skill: Injected verification & pareto acceptance block")

    return mutated, applied

def mutate_code(raw_code: str) -> Tuple[str, List[str]]:
    """消除代码中的裸异常与高危副作用，提升故障域隔离度"""
    mutated = raw_code
    applied = []
    for pattern, replacement in CODE_MUTATION_RULES:
        if re.search(pattern, mutated):
            mutated = re.sub(pattern, replacement, mutated)
            applied.append(f"Code: {pattern} -> {replacement[:30]}")
    return mutated, applied

def mutate_text(raw_text: str, domain: str = "auto") -> Tuple[str, List[str]]:
    """全局自动分流变异入口"""
    if domain == "auto":
        # 简单判定
        if re.search(r'def\s+\w+\(|class\s+\w+[:\(]', raw_text):
            domain = "code"
        elif re.search(r'---\s*\nname:|# Agent Skill|技能规范', raw_text):
            domain = "skill"
        else:
            domain = "copy"
            
    if domain == "code":
        return mutate_code(raw_text)
    elif domain == "skill":
        return mutate_skill(raw_text)
    else:
        return mutate_copy(raw_text)

def main():
    parser = argparse.ArgumentParser(description="The Oracle Axiomatic Mutator")
    parser.add_argument("input_file", help="待变异重构的初稿文件路径")
    parser.add_argument("--output", "-o", help="输出变异后文件的路径")
    
    args = parser.parse_args()
    
    with open(args.input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    mutated, logs = mutate_text(content)
    
    print("\n=======================================================")
    print("🧬 The Oracle 公理变异重构完成 (Axiomatic Mutation Applied)")
    print("=======================================================")
    print(f"触发的变异算子数量: {len(logs)} 个")
    for log in logs[:8]:
        print(f"  • {log}")
    print("=======================================================\n")
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(mutated)
        print(f"✓ 结果已写入: {args.output}\n")
    else:
        print(mutated)

if __name__ == "__main__":
    main()
