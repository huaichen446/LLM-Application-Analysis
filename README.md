<div align="right">

**[🇬🇧 English](README.md)** | **[🇷🇺 Русский](README.ru.md)** | **[🇨🇳 中文](README.zh.md)**

</div>

# 🧠 Application & Output Analysis of Large Language Models (LLMs)

---

## 📘 Project Overview

This project aims to analyze the **applications and output behavior of Large Language Models (LLMs)** across various domains.  
By collecting and analyzing data from multiple sources (Arxiv, Reddit, Kaggle, etc.), we seek to:

- 📊 Track the research and industrial trends of LLMs  
- 💬 Explore how prompt structure affects output quality  
- 🌐 Examine public discussions about LLMs on social media  
- 🔮 Predict the most promising application fields for the next 3 years  

---

## 👥 Authors & Group

**Authors:** Zhao Chenhao · Chen Weipeng · Wang Xuanyu  
**Group:** 5140904/50102 · 5140904/50101  

---

## 📑 Table of Contents

- [📘 Project Overview](#-project-overview)  
- [📊 Current Progress](#-current-progress-as-of-october-2025)  
- [🧩 Ongoing Analytical Tasks](#-ongoing-analytical-tasks)  
- [📂 Datasets](#-datasets)  
- [🧱 Project Structure](#-project-structure)  
- [🎯 Project Goals](#-project-goals)

---

## 📊 Current Progress (as of October 2025)

**✅ Data collection tasks completed:**

| Task | Description | Status |
|------|--------------|--------|
| 🏭 Industry Statistics | Collected LLM-related publication data across various industries (education, healthcare, finance, etc.) | ✅ Done |
| 📈 Research Trends | Gathered Arxiv publication counts and keyword frequencies | ✅ Done |
| 💬 Prompt Structure | Built a dataset of prompts for quality analysis | ✅ Done |
| 🌐 Social Platform Analysis | Sampled Reddit discussions related to LLM applications | ✅ Done |

**Next step:**  
> Conduct **exploratory data analysis (EDA)** and visualization using Jupyter Notebooks.

---

## 🧩 Ongoing Analytical Tasks

1. **📚 Industry Trend Analysis** — Analyze LLM adoption trends in education, healthcare, finance, science, and entertainment over the past five years.  
   🟢 *Data collected*

2. **📊 Research Trend Tracking** — Study annual growth of LLM-related publications and frequency of key terms (*alignment, efficiency, reasoning*).  
   🟢 *Data collected*

3. **🧠 Prompt Structure & Output Quality** — Examine how prompt phrasing impacts coherence, reasoning, and factual accuracy of responses.  
   🟢 *Dataset prepared*

4. **💭 Social Discussion Analysis** — Compare purposes of using LLMs among different user groups (developers, students, researchers) on Reddit.  
   🟢 *Data collected*

5. **🔮 Future Field Prediction** — Predict the most promising LLM application domains over the next three years.  
   🔸 *Pending*

---

## 📂 Datasets

All datasets are stored under the `/data` directory.  

| Filename | Description | Source / Script |
|-----------|-------------|----------------|
| **`arxiv_stats_by_industry.csv`** | Annual publication counts of LLM papers by industry | `scripts/collect_publication_stats.py` |
| **`arxiv_trends_by_month.csv`** | Monthly Arxiv trends and frequency of key terms (*alignment, efficiency, reasoning*) | `scripts/collect_arxiv_trends.py` |
| **`prompt_examples_dataset.csv`** | Dataset of various prompt types for analyzing output quality | Kaggle · Prompt Engineering Dataset |
| **`realm_reddit_sample_raw.csv`** | Reddit subset from Hugging Face “kkChimmy/REALM”, 2,000 samples on LLM usage discussions | `scripts/collect_reddit_data.py` |

---

## 🧱 Project Structure

```bash
LLM-Application-Analysis/
│
├── data/              # Datasets
├── notebooks/         # EDA & Visualization Notebooks
├── scripts/           # Data collection and preprocessing scripts
├── results/           # Final charts and analytical outputs
└── docs/              # Additional documentation and notes
