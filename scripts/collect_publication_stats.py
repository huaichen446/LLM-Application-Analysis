import requests
import pandas as pd
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET
from time import sleep

SEARCH_QUERIES = {
    "education": '(large language model OR LLM OR "LL models" OR AI) AND (education OR student OR learning OR teaching OR edtech)',
    "medicine": '(large language model OR LLM OR "LL models" OR AI) AND (medicine OR medical OR healthcare OR health OR patient)',
    "finance": '(large language model OR LLM OR "LL models" OR AI) AND (finance OR financial OR stock OR investment OR banking OR economy)',
    "science": '(large language model OR LLM OR "LL models" OR AI) AND (science OR research OR discovery OR biology OR physics OR chemistry OR data)',
    "entertainment": '(large language model OR LLM OR "LL models" OR AI) AND (entertainment OR gaming OR movie OR music OR media OR game OR film)',
}


START_YEAR = 2020
END_YEAR = datetime.now().year

def get_arxiv_count(query):
    url = "https://export.arxiv.org/api/query"
    params = {"search_query": query, "max_results": 0}
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        root = ET.fromstring(resp.text)
        total = int(root.find("{http://a9.com/-/spec/opensearch/1.1/}totalResults").text)
        return total
    except Exception as e:
        print(f"  > 查询失败 ({e})")
        return None

results_list = []
for year in range(START_YEAR, END_YEAR + 1):
    for industry, query in SEARCH_QUERIES.items():
        full_query = f'({query}) AND submittedDate:[{year}0101 TO {year}1231]'
        print(f"正在搜索: 年份={year}, 行业={industry} ...")
        total = get_arxiv_count(full_query)
        print(f"  > 找到 {total} 篇论文")
        results_list.append({
            "year": year,
            "industry": industry,
            "publication_count": total,
            "query": full_query,
            "timestamp": datetime.now().isoformat()
        })
        sleep(0.5)

df = pd.DataFrame(results_list)
output_path = Path(__file__).parent.parent / "data" / "raw" / "arxiv_stats_by_industry.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)
print(f"✅ 数据保存到: {output_path}")
