<div align="right">

**[🇬🇧 English](README.md)** | **[🇷🇺 Русский](README.ru.md)** | **[🇨🇳 中文](README.zh.md)**

</div>

# 🧠 LLM 应用与输出分析 (Application & Output Analysis of Large Language Models)

---

## 📘 项目简介

本项目致力于分析 **大语言模型（Large Language Models, LLM）** 在不同领域的应用及其输出结果。  
我们通过多源数据（Arxiv、Reddit、Kaggle等）研究 LLM 的发展趋势、应用现状与未来潜力，旨在：

- 📊 追踪 LLM 的研究与行业动态  
- 💬 探索提示词结构对输出质量的影响  
- 🌐 分析社交平台中 LLM 的使用讨论  
- 🔮 预测未来 3 年最具潜力的应用方向  

---

## 👥 作者与小组信息

**作者：** 赵晨浩 · 陈伟鹏 · 王瑄予  
**小组：** 5140904/50102 · 5140904/50101  

---

## 📑 目录

- [📘 项目简介](#-项目简介)
- [📊 当前进展](#-当前进展截至-2025-年-10-月)
- [🧩 待解决的分析任务](#-待解决的分析任务)
- [📂 数据集说明](#-数据集说明)
- [🧱 项目结构](#-项目结构)
- [🎯 项目目标总结](#-项目目标总结)

---

## 📊 当前进展（截至 2025 年 10 月）

**✅ 已完成的数据收集任务：**

| 任务 | 内容 | 状态 |
|------|------|------|
| 🏭 行业统计 | 收集不同行业（教育、医疗、金融等）的论文数据 | ✅ 已完成 |
| 📈 研究趋势 | 抓取 Arxiv 上论文数量与关键词趋势 | ✅ 已完成 |
| 💬 提示词结构 | 构建用于输出分析的提示词数据集 | ✅ 已完成 |
| 🌐 社交平台分析 | 抽样 Reddit 上 LLM 相关讨论 | ✅ 已完成 |

| 阶段 | 内容 | 状态 |
|------|------|------|
| 🏭 数据收集 | 完成来自 Arxiv、Reddit、Kaggle 等多源数据的收集 | ✅ 已完成 |
| 🧹 数据清洗 | 对各数据集进行格式统一与缺失值处理 | ✅ 已完成 |
| 🧩 数据集整合 | 构建统一分析用的多模态数据结构 | ✅ 已完成 |
| 📊 初步分析 | 在 Jupyter Notebooks 中开展探索性数据分析（EDA）与可视化 | ✅ 已完成 |


---

## 📂 数据集说明

所有数据均存放于 `/data` 目录中。  

| 文件名 | 描述 | 来源脚本 / 来源 |
|--------|------|----------------|
| **`arxiv_stats_by_industry.csv`** | LLM 在各行业（教育、医疗、金融等）的年度论文统计 | `scripts/collect_publication_stats.py` |
| **`arxiv_trends_by_month.csv`** | Arxiv 上 LLM 论文月度趋势与关键词频率（alignment, efficiency, reasoning） | `scripts/collect_arxiv_trends.py` |
| **`prompt_examples_dataset.csv`** | 含不同类型提示词样本的数据集，用于分析输出质量 | Kaggle · Prompt Engineering Dataset |
| **`realm_reddit_sample_raw.csv`** | 来自 Hugging Face “kkChimmy/REALM” Reddit 子集，采样 2000 条与 LLM 使用相关讨论 | `scripts/collect_reddit_data.py` |

---

## 🧱 项目结构

```bash
LLM-Application-Analysis/
│
├── data/              # 所有数据集
├── notebooks/         # EDA 与可视化的 Jupyter Notebooks
├── scripts/           # 数据收集与清洗脚本
├── results/           # 输出图表与分析结果
└── docs/              # 附加文档与笔记
