#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Oracle (先知) - Executable Sparse MoE Gating Router (门控路由调度引擎)
==========================================================================
Maps any user task, problem statement, or file artifact to the top K (2~3)
most relevant Grand Axiom Domains (out of 24) and canonical Mental Models
(out of 120), outputting a deterministic `router_diagnosis` contract.

Zero third-party dependencies (Pure Python 3 Standard Library).
"""

import argparse
import json
import os
import re
import sys
from typing import Any, Dict, List


EXPERT_DOMAINS: List[Dict[str, Any]] = [
    {
        "id": 1,
        "slug": "game-theory",
        "file": "experts/game-theory.md",
        "name": "博弈论与信号学 (Game Theory & Signaling)",
        "axioms": ["扎哈维昂贵信号理论 (Costly Signaling)", "纳什均衡与机制设计 (Nash Equilibrium)", "阿克塞尔罗德重复博弈 (Tit-for-Tat)"],
        "models": ["88", "91", "92", "93"],
        "keywords": ["博弈", "信任", "背书", "吹牛", "自嗨", "信号", "资质", "药厂", "检验", "合作", "囚徒困境", "纳什", "质押", "公关", "PR", "转化", "客户信任", "signaling", "trust", "game"],
    },
    {
        "id": 2,
        "slug": "information-physics",
        "file": "experts/information-physics.md",
        "name": "信息论与计算物理学 (Information Theory & Physics)",
        "axioms": ["香农信息熵与信噪比 (Shannon SNR)", "特斯勒复杂度守恒定律 (Tesler's Law)", "幂等性与纯函数状态机 (Idempotence)"],
        "models": ["56", "57", "60"],
        "keywords": ["信息熵", "信噪比", "黑话", "套话", "公文", "废话", "冗长", "提纯", "精简", "代码", "重构", "复杂度", "幂等", "函数", "耦合", "赋能", "抓手", "闭环", "snr", "entropy", "refactor", "code"],
    },
    {
        "id": 3,
        "slug": "cognitive-neuro",
        "file": "experts/cognitive-neuro.md",
        "name": "认知神经与传播心理学 (Cognitive Neuroscience)",
        "axioms": ["说服知识模型 (PKM 防御拆解)", "双重编码与具象画面律 (Dual-Coding)", "三元神经递质动力学 (皮质醇/催产素/多巴胺)", "巴德利听觉语音回路 (28字气口红线)"],
        "models": ["76", "77", "78", "79"],
        "keywords": ["口播", "文案", "脚本", "黄金3秒", "完播率", "划走", "共情", "大脑", "神经", "多巴胺", "催产素", "皮质醇", "防备", "营销感", "呼吸", "气口", "短视频", "演讲", "文章", "copy", "script"],
    },
    {
        "id": 4,
        "slug": "economics-pareto",
        "file": "experts/economics-pareto.md",
        "name": "经济学与帕累托决策学 (Economics & Pareto)",
        "axioms": ["帕累托最优前沿 (Pareto Frontier)", "机会成本与沉没成本免疫 (Opportunity Cost)", "边际成本递减与规模复利 (Marginal Cost)", "经济护城河 (Economic Moats)"],
        "models": ["45", "90"],
        "keywords": ["帕累托", "成本", "收益", "ROI", "预算", "护城河", "复利", "商业模式", "定价", "变现", "沉没成本", "机会成本", "权衡", "资源分配", "pareto", "economics", "roi"],
    },
    {
        "id": 5,
        "slug": "evolutionary-social",
        "file": "experts/evolutionary-social.md",
        "name": "演化生物学与社会物理学 (Evolutionary & Social Physics)",
        "axioms": ["敦巴数与声波梳毛假说 (Vocal Grooming)", "高斯竞争排斥与生态位分化 (Ecological Niche)", "红皇后协同演化效应 (Red Queen Effect)"],
        "models": ["61", "62", "63", "64", "65", "66", "69"],
        "keywords": ["内卷", "同质化", "差异化", "生态位", "人设", "私域", "社群", "粉丝", "温度", "人味", "演化", "竞争", "蓝海", "红海", "物种", "共生", "niche", "evolution"],
    },
    {
        "id": 6,
        "slug": "complex-systems",
        "file": "experts/complex-systems.md",
        "name": "复杂系统与控制论 (Complex Systems & Cybernetics)",
        "axioms": ["盖尔定律 (Gall's Law)", "正负反馈回路与耗散结构 (Feedback Loops)", "二阶思维与古德哈特反作弊 (Second-Order Thinking)", "高德拉特约束理论 (TOC 瓶颈律)"],
        "models": ["04", "33", "34", "58", "59", "67", "68", "106"],
        "keywords": ["系统", "架构", "飞轮", "瓶颈", "短板", "木桶", "反馈", "失控", "雪崩", "指标", "KPI", "OKR", "二阶", "连锁反应", "控制论", "演进", "system", "bottleneck", "architecture"],
    },
    {
        "id": 7,
        "slug": "logical-razors",
        "file": "experts/logical-razors.md",
        "name": "逻辑剃刀与逆向思维 (Logical Razors & Inversion)",
        "axioms": ["芒格逆向思维 (Jacobi-Munger Inversion)", "四大哲学剃刀 (奥卡姆/波普尔/汉隆/希钦斯)", "洛拉帕卢扎共振效应 (Lollapalooza)"],
        "models": ["02", "06", "07", "08", "14", "17", "19", "20", "81", "86"],
        "keywords": ["逆向", "反过来", "避坑", "剃刀", "奥卡姆", "证伪", "死因", "事前验尸", "极简", "激励", "共振", "第一性原理", "本质", "inversion", "razor"],
    },
    {
        "id": 8,
        "slug": "causality-bayes",
        "file": "experts/causality-bayes.md",
        "name": "因果推断与贝叶斯认识论 (Causality & Bayesian Epistemology)",
        "axioms": ["朱迪亚·珀尔因果阶梯 (观察/干预/反事实)", "混杂因子隔离与辛普森悖论 (Confounders)", "贝叶斯先验与似然比更新 (Bayesian Updating)"],
        "models": ["18", "41", "46", "48", "49"],
        "keywords": ["因果", "相关", "归因", "复盘", "为什么", "真相", "混杂", "幸存者偏差", "贝叶斯", "概率", "统计", "A/B测试", "反事实", "根因", "causality", "bayes", "root cause"],
    },
    {
        "id": 9,
        "slug": "antifragility-security",
        "file": "experts/antifragility-security.md",
        "name": "反脆弱与安全攻防工程 (Antifragility & Adversarial Security)",
        "axioms": ["塔勒布反脆弱与杠铃策略 (Antifragility & Convexity)", "肌肤之亲公理 (Skin in the Game)", "拜占庭容错与零信任红队架构 (Zero-Trust Red-Teaming)"],
        "models": ["40", "43", "97", "98"],
        "keywords": ["反脆弱", "黑天鹅", "风险", "安全", "合规", "广告法", "封号", "漏洞", "注入", "越狱", "兜底", "容灾", "防御", "红队", "压测", "security", "compliance", "risk", "antifragile"],
    },
    {
        "id": 10,
        "slug": "multimodal-physics",
        "file": "experts/multimodal-physics.md",
        "name": "多模态视听与运动物理学 (Multimodal & Cinematic Physics)",
        "axioms": ["普多夫金音画对位律 (Audio-Visual Counterpoint)", "视网膜运动熵与切率定律 (1.5~4.0s Cut Rate)", "声学包络与侧链闪避定律 (-18dBFS Sidechain Ducking)"],
        "models": ["78", "79"],
        "keywords": ["视频", "剪辑", "分镜", "镜头", "画面", "字幕", "BGM", "配乐", "音画", "B-Roll", "分贝", "切镜", "视觉", "导演", "成片", "video", "audio", "cinematic"],
    },
    {
        "id": 11,
        "slug": "behavioral-heuristics",
        "file": "experts/behavioral-heuristics.md",
        "name": "行为经济学与启发式偏见 (Behavioral Economics & Heuristics)",
        "axioms": ["卡尼曼双系统模型 (System 1 & System 2)", "前景理论与 2.5 倍损失厌恶 (Prospect Theory)", "心理账户与锚定效应 (Mental Accounting & Anchoring)", "泰勒助推与默认选项效应 (Nudge & Default)"],
        "models": ["37", "71", "72", "73", "74", "80"],
        "keywords": ["行为经济", "直觉", "损失厌恶", "锚定", "心理账户", "助推", "默认", "下单", "促单", "价格锚点", "痛点", "犹豫", "摩擦", "nudge", "heuristic"],
    },
    {
        "id": 12,
        "slug": "computation-network",
        "file": "experts/computation-network.md",
        "name": "计算理论与复杂网络科学 (Computation & Network Science)",
        "axioms": ["图灵停机边界与哥德尔不完备 (Halting & Incompleteness)", "P vs NP 启发式剪枝 (Heuristic Pruning)", "巴拉巴西无标度网络与幂律分布 (Scale-Free Power Laws)", "布鲁尔 CAP 定理 (Distributed Trade-off)"],
        "models": ["09", "47", "50", "51", "52", "53", "54", "55"],
        "keywords": ["算法", "算力", "网络效应", "裂变", "病毒传播", "节点", "KOL", "分布式", "并发", "死循环", "停机", "幂律", "二八法则", "图灵", "哥德尔", "network", "algorithm", "distributed"],
    },
    {
        "id": 13,
        "slug": "strategy-ooda",
        "file": "experts/strategy-ooda.md",
        "name": "大战略与动态竞争博弈 (Grand Strategy & OODA Loop)",
        "axioms": ["博伊德 OODA 快速决策环 (OODA Loop)", "克劳塞维茨重心法则与战争迷雾 (Schwerpunkt)", "孙子兵法奇正相生与虚实之道 (Shaping the Battlefield)", "克里斯坦森破坏性创新 (Disruptive Innovation)"],
        "models": ["36", "38", "94", "95", "96"],
        "keywords": ["战略", "打法", "破局", "竞争", "对手", "巨头", "降维", "颠覆", "奇兵", "重心", "OODA", "护城河", "战役", "突围", "strategy", "competitor", "disrupt"],
    },
    {
        "id": 14,
        "slug": "thermodynamics-statistical",
        "file": "experts/thermodynamics-statistical.md",
        "name": "热力学与统计物理 (Thermodynamics & Statistical Mechanics)",
        "axioms": ["玻尔兹曼熵增定律与薛定谔负熵流 (Negentropy)", "普里戈金耗散结构与相变临界 (Dissipative Structures)", "遍历性与破产吸收态公理 (Ergodicity vs Ruin)", "最小作用量原理 (Least Action)"],
        "models": ["31", "32", "35", "42"],
        "keywords": ["熵增", "负熵", "耗散", "混乱", "腐败", "老化", "破产", "爆仓", "遍历性", "相变", "临界点", "活力", "组织涣散", "thermodynamics", "ergodicity", "ruin"],
    },
    {
        "id": 15,
        "slug": "semiotics-language",
        "file": "experts/semiotics-language.md",
        "name": "符号学与语言哲学 (Semiotics & Philosophy of Language)",
        "axioms": ["维特根斯坦语言游戏与边界律 (Language Games)", "奥斯汀言语行为理论 (Speech Act Theory)", "皮尔斯三元符号学 (Icon/Index/Symbol)", "莱考夫概念隐喻与具身认知 (Embodied Metaphor)"],
        "models": ["115", "116"],
        "keywords": ["符号", "隐喻", "比喻", "修辞", "命名", "口号", "Slogan", "品牌词", "概念", "定义", "语言", "话术", "台词", "意象", "metaphor", "semiotics", "naming"],
    },
    {
        "id": 16,
        "slug": "lateral-breakthrough",
        "file": "experts/lateral-breakthrough.md",
        "name": "破框思维与创造性突破 (Think Out of the Box & TRIZ)",
        "axioms": ["九点谜题隐性假设粉碎律 (Assumption Busting)", "德博诺横向思维与 PO 挑衅算子 (Lateral Thinking)", "瓦茨拉维克二阶改变 (Second-Order Change)", "TRIZ 矛盾分离与最终理想解 (IFR)", "正交升维打击 (Orthogonal Dimensionality)"],
        "models": ["25", "26", "27", "28", "29", "30"],
        "keywords": ["破框", "创新", "创意", "脑洞", "死局", "两难", "既要又要", "矛盾", "横向思维", "TRIZ", "二阶改变", "升维", "跳出盒子", "out of the box", "lateral", "creative", "triz"],
    },
    {
        "id": 17,
        "slug": "epistemic-latticework",
        "file": "experts/epistemic-latticework.md",
        "name": "认知格栅与心智偏见免疫 (Mental Models Latticework & Cognitive Immunity)",
        "axioms": ["科齐布斯基“地图不是疆域” (Map != Territory)", "芒格 25 种人类误判心理学防御 (Misjudgment Immunity)", "巴菲特能力圈与达克效应防护 (Circle of Competence)", "局部最优陷阱与模拟退火跳跃 (Simulated Annealing)"],
        "models": ["03", "05", "39", "44", "70", "75", "82", "83", "84", "85", "87", "89"],
        "keywords": ["偏见", "盲区", "误判", "执念", "地图不是疆域", "能力圈", "达克效应", "局部最优", "思维模型", "芒格", "认知升级", "自省", "bias", "munger", "latticework"],
    },
    {
        "id": 18,
        "slug": "dialectical-thinking",
        "file": "experts/dialectical-thinking.md",
        "name": "辩证法与矛盾演进律 (Dialectical Thinking & Aufheben)",
        "axioms": ["黑格尔正反合三元辩证与扬弃 (Aufheben)", "唯物辩证三大规律 (对立统一/质量互变/否定之否定)", "苏格拉底反诘产婆术 (Socratic Elenchus)", "东方道家阴阳转化与玻姆深度汇谈 (Yin-Yang & Bohm Dialogue)"],
        "models": ["10", "21", "22", "23", "24"],
        "keywords": ["辩证", "正反合", "扬弃", "矛盾", "对立统一", "量变质变", "否定之否定", "苏格拉底", "阴阳", "物极必反", "折中", "妥协", "dialectic", "aufheben", "synthesis"],
    },
    {
        "id": 19,
        "slug": "critical-reasoning",
        "file": "experts/critical-reasoning.md",
        "name": "批判性思考与图尔敏论证 (Critical Thinking & Argumentation)",
        "axioms": ["保罗-埃尔德批判性思维框架 (8要素×9标准)", "图尔敏六要素论证模型 (Toulmin Model)", "皮尔士演绎/归纳/溯因三联环 (Abductive Reasoning)", "逻辑谬误解剖刀 (20+ Fallacies)"],
        "models": ["11", "12", "13", "15", "16"],
        "keywords": ["批判性", "论证", "图尔敏", "逻辑漏洞", "谬误", "诡辩", "反驳", "证据", "推理", "前提", "结论", "严谨", "审稿", "辩论", "critical", "toulmin", "fallacy", "argument"],
    },
    {
        "id": 20,
        "slug": "ethics-social-contract",
        "file": "experts/ethics-social-contract.md",
        "name": "伦理对齐与社会契约论 (Ethics Alignment & Social Contract)",
        "axioms": ["罗尔斯无知之幕与最大最小原则 (Veil of Ignorance & Maximin)", "康德绝对命令：人是目的而非工具 (Humanity as an End)", "外部性内部化与社会总福利函数 (Social Welfare)", "委托代理问题与激励相容对齐 (Incentive Compatibility)"],
        "models": ["99", "100"],
        "keywords": ["伦理", "道德", "正义", "公平", "割韭菜", "欺诈", "隐私", "价值观", "社会责任", "向善", "罗尔斯", "康德", "对齐", "弱势群体", "ethics", "alignment", "fairness"],
    },
    {
        "id": 21,
        "slug": "system-archetypes",
        "file": "experts/system-archetypes.md",
        "name": "系统动力学基模与梅多斯杠杆点 (System Archetypes & Leverage Points)",
        "axioms": ["德内拉·梅多斯 12 大系统干预杠杆点 (12 Leverage Points)", "舍本逐末与饮鸩止渴基模 (Shifting the Burden)", "成长上限基模 (Limits to Growth)", "目标侵蚀与公地悲剧基模 (Drifting Goals & Tragedy of Commons)"],
        "models": ["101", "102", "103", "104", "105"],
        "keywords": ["杠杆点", "梅多斯", "系统基模", "第五项修炼", "舍本逐末", "饮鸩止渴", "成长上限", "目标侵蚀", "公地悲剧", "治标不治本", "成瘾", "范式转移", "leverage", "archetype"],
    },
    {
        "id": 22,
        "slug": "lean-experimentation",
        "file": "experts/lean-experimentation.md",
        "name": "精益实验、探索-利用与刻意练习 (Lean Experimentation & Deliberate Practice)",
        "axioms": ["多臂老虎机探索-利用权衡与 UCB (Explore vs Exploit)", "精益创业 MVP 构建-测量-学习飞轮 (Build-Measure-Learn)", "费曼学习法与去术语测试 (Feynman Technique)", "艾利克森刻意练习与高阶心理表征 (Deliberate Practice)"],
        "models": ["107", "108", "109", "110"],
        "keywords": ["MVP", "精益", "小步快跑", "验证", "实验", "探索", "利用", "老虎机", "费曼", "大白话", "降维解释", "刻意练习", "心理表征", "训练", "lean", "experiment", "feynman"],
    },
    {
        "id": 23,
        "slug": "narrative-aesthetics",
        "file": "experts/narrative-aesthetics.md",
        "name": "叙事动力学、英雄之旅与峰终美学 (Narrative Dynamics & Peak-End Aesthetics)",
        "axioms": ["坎贝尔英雄之旅与智者导师定位 (The Hero's Journey)", "亚里士多德三幕剧与卡塔西斯净化 (Three-Act & Catharsis)", "蔡加尼克悬念效应与格式塔闭合 (Zeigarnik Open Loop)", "卡尼曼峰终定律与过程忽视 (Peak-End Rule)"],
        "models": ["111", "112", "113", "114"],
        "keywords": ["故事", "叙事", "英雄之旅", "悬念", "钩子", "高潮", "峰终定律", "体验", "情绪曲线", "反转", "结局", "金句", "戏剧", "story", "narrative", "hook", "peak-end"],
    },
    {
        "id": 24,
        "slug": "category-isomorphism",
        "file": "experts/category-isomorphism.md",
        "name": "范畴论同构、规模法则与不变量 (Category Isomorphism & Scaling Invariants)",
        "axioms": ["范畴论与跨学科函子同构映射 (Functorial Isomorphism)", "诺特定理与贝索斯十年战略不变量 (Strategic Invariants)", "韦斯特规模法则与异速生长幂律 (West's Scaling Laws)", "冯·诺依曼自复制自动机与奇异环 (Self-Replicating Strange Loops)"],
        "models": ["117", "118", "119", "120"],
        "keywords": ["同构", "范畴论", "跨学科", "不变量", "十年不变", "贝索斯", "规模法则", "自进化", "自举", "奇异环", "元技能", "自我迭代", "isomorphism", "invariant", "scaling", "bootstrap"],
    },
]


def detect_domain_category(text: str) -> str:
    """Detect the primary evaluation category from query or text."""
    t_lower = text.lower()
    if any(k in t_lower for k in ["skill.md", "公理", "门控路由", "自举", "agent", "prompt", "元技能"]):
        return "skill"
    if any(k in t_lower for k in ["def ", "class ", "import ", "代码", "重构", "函数", "架构", "并发"]):
        return "code"
    if any(k in t_lower for k in ["图尔敏", "辩证", "批判性", "逻辑谬误", "论证", "正反合", "因此", "诚然"]):
        return "reasoning"
    if any(k in t_lower for k in ["战略", "商业模式", "破局", "竞争", "护城河", "roi", "ooda"]):
        return "strategy"
    return "copy"


def route_task(query_or_text: str, top_k: int = 3) -> Dict[str, Any]:
    """
    Score all 24 Grand Axiom Domains against the input text and return
    a structured `router_diagnosis` dictionary.
    """
    top_k = max(2, min(6, top_k))
    text_lower = query_or_text.lower()
    category = detect_domain_category(query_or_text)

    scored_experts: List[Dict[str, Any]] = []
    for exp in EXPERT_DOMAINS:
        score = 0
        matched_keywords: List[str] = []
        for kw in exp["keywords"]:
            if kw.lower() in text_lower:
                score += 10
                matched_keywords.append(kw)

        # Category affinity priors (Bayesian base rate boost)
        if category == "copy" and exp["slug"] in ("cognitive-neuro", "game-theory", "information-physics", "narrative-aesthetics", "antifragility-security"):
            score += 4
        elif category == "code" and exp["slug"] in ("information-physics", "computation-network", "complex-systems", "antifragility-security"):
            score += 4
        elif category == "strategy" and exp["slug"] in ("strategy-ooda", "economics-pareto", "lateral-breakthrough", "system-archetypes", "game-theory"):
            score += 4
        elif category == "reasoning" and exp["slug"] in ("critical-reasoning", "dialectical-thinking", "logical-razors", "causality-bayes", "ethics-social-contract"):
            score += 4
        elif category == "skill" and exp["slug"] in ("category-isomorphism", "system-archetypes", "computation-network", "information-physics", "critical-reasoning"):
            score += 4

        scored_experts.append({
            "id": exp["id"],
            "slug": exp["slug"],
            "file": exp["file"],
            "name": exp["name"],
            "score": score,
            "matched_keywords": matched_keywords,
            "axioms": exp["axioms"],
            "mental_model_ids": exp["models"],
        })

    scored_experts.sort(key=lambda x: (-x["score"], x["id"]))
    selected = scored_experts[:top_k]

    # Collect unique mental model IDs activated
    activated_models: List[str] = []
    for item in selected:
        for mid in item["mental_model_ids"]:
            if mid not in activated_models:
                activated_models.append(mid)

    pareto_vectors = {
        "copy": ["V1_shannon_snr (香农信噪比)", "V2_impact_signaling (扎哈维硬核冲击力)", "V3_compliance (反脆弱合规安全度)", "V4_acoustic_flow (巴德利听觉流畅度)"],
        "code": ["V1_structural_modularity (结构模块化)", "V2_type_and_doc_clarity (类型与文档自解释)", "V3_defensive_safety (拜占庭防御鲁棒性)", "V4_idiomatic_simplicity (奥卡姆极简度)"],
        "strategy": ["V1_first_principles_depth (第一性原理穿透力)", "V2_pareto_leverage (高杠杆ROI)", "V3_antifragile_moat (反脆弱护城河)", "V4_execution_clarity (可验证执行颗粒度)"],
        "reasoning": ["V1_toulmin_completeness (图尔敏论证完备度)", "V2_dialectical_synthesis (黑格尔辩证扬弃度)", "V3_fallacy_immunity (逻辑谬误免疫度)", "V4_ethical_alignment (罗尔斯/康德伦理对齐度)"],
        "skill": ["V1_directive_density (可执行指令密度)", "V2_boundary_safety (图灵停机与红队防御边界)", "V3_verification_rigor (波普尔可证伪验证闭环)", "V4_axiomatic_grounding (24大公理与120模型锚定深度)"],
    }

    return {
        "router_diagnosis": {
            "detected_category": category,
            "total_expert_pool_size": len(EXPERT_DOMAINS),
            "total_mental_models_indexed": 120,
            "three_questions": {
                "q1_physical_essence": f"当前任务属于 [{category.upper()}] 域，需剥离表象话术，直击第一性原理与客观状态转移。",
                "q2_core_contradiction": f"激活 [{selected[0]['name']}] 与 [{selected[1]['name']}] 进行正交破框与辩证扬弃，拒绝平庸折中。",
                "q3_strategic_invariants": "严守帕累托四维单调不降铁律 (∀i: ΔVi >= 0, ∃j: ΔVj > 0) 与合规伦理底线。",
            },
            "selected_experts": selected,
            "activated_mental_model_ids": activated_models,
            "pareto_vector_definition": pareto_vectors.get(category, pareto_vectors["copy"]),
        }
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="The Oracle - Sparse MoE Gating Router (24 Experts / 120 Models)")
    parser.add_argument("target", help="Task description string or path to a file")
    parser.add_argument("--top-k", type=int, default=3, help="Number of experts to activate (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON contract")
    args = parser.parse_args()

    if os.path.isfile(args.target):
        with open(args.target, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = args.target

    result = route_task(content, top_k=args.top_k)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        diag = result["router_diagnosis"]
        print("=" * 72)
        print("🧭 The Oracle (先知) — 门控路由诊断报告 (Sparse MoE Router Diagnosis)")
        print("=" * 72)
        print(f"📂 识别领域 (Category)       : {diag['detected_category'].upper()}")
        print(f"🏛  专家池规模 (Expert Pool) : {diag['total_expert_pool_size']} 大先知公理领域 / {diag['total_mental_models_indexed']} 大人类思维模型")
        print("-" * 72)
        print("🔥 激活专家组合 (Activated Top-K Experts):")
        for idx, exp in enumerate(diag["selected_experts"], 1):
            kws = ", ".join(exp["matched_keywords"][:5]) if exp["matched_keywords"] else "领域先验基线"
            print(f"  {idx}. [{exp['slug']}] {exp['name']} (权重分: {exp['score']})")
            print(f"     ├─ 路径: {exp['file']}")
            print(f"     ├─ 命中特征: {kws}")
            print(f"     └─ 核心公理: {' / '.join(exp['axioms'])}")
        print("-" * 72)
        print(f"🧠 关联思维模型编号 (Mental Models): {', '.join('#' + m for m in diag['activated_mental_model_ids'])}")
        print("📐 帕累托四维评价向量 (4D Pareto Vector):")
        for vec in diag["pareto_vector_definition"]:
            print(f"  • {vec}")
        print("=" * 72)


if __name__ == "__main__":
    main()
