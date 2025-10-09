import arxiv
import pandas as pd
from datetime import datetime
from pathlib import Path
import re
import calendar # To get the number of days in a month
from arxiv import UnexpectedEmptyPageError

# BASE_QUERY and KEYWORDS remain the same
BASE_QUERY = '(' + ' OR '.join([
    '"large language model"', '"LLM"', '"foundation model"', '"language model"',
    '"transformer model"', '"instruction-tuned model"', '"chat model"',
    '"text generation"', '"autoregressive model"', '"pretrained language model"',
    '"instruction fine-tuned model"', '"chatbot model"', '"conversational AI"'
]) + ')'

KEYWORDS = ["alignment", "efficiency", "reasoning", "prompt", "chain-of-thought", "RLHF",
            "safety", "robustness", "scaling", "few-shot", "zero-shot", "fine-tuning",
            "instruction tuning", "evaluation", "capabilities", "bias", "fairness",
            "hallucination", "interpretability", "reinforcement learning", "RL",
            "multi-modal", "knowledge", "planning", "coherence", "memory", "generalization",
            "transfer learning", "adversarial", "optimization", "performance", "compression"]

START_YEAR = 2010
END_YEAR = datetime.now().year

trends_list = []
client = arxiv.Client(page_size=200, delay_seconds=3.0, num_retries=3) # Increased page size slightly

for year in range(START_YEAR, END_YEAR + 1):
    print(f"\nProcessing year: {year}...")
    
    # Initialize containers to accumulate data for the entire year
    total_results_for_year = 0
    keyword_counts_for_year = {k: 0 for k in KEYWORDS}

    # ✨ NEW: Loop through each month of the year
    for month in range(1, 13):
        month_str = f"{month:02d}" # Format month as 01, 02, etc.
        
        # Determine the first and last day of the month
        start_day = "01"
        last_day = str(calendar.monthrange(year, month)[1])
        
        print(f"  > Searching month: {year}-{month_str}...")

        # ✨ NEW: Create a query for the specific month
        query_with_month = (
            f"({BASE_QUERY}) AND "
            f"submittedDate:[{year}{month_str}{start_day} TO {year}{month_str}{last_day}]"
        )
        
        search = arxiv.Search(
            query=query_with_month,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            max_results=40000 # High limit per month as a safeguard
        )
        
        monthly_paper_count = 0
        try:
            for result in client.results(search):
                monthly_paper_count += 1
                abstract = result.summary.lower()
                for keyword in KEYWORDS:
                    pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
                    matches = re.findall(pattern, abstract)
                    keyword_counts_for_year[keyword] += len(matches)

            # Add this month's count to the year's total
            total_results_for_year += monthly_paper_count
            if monthly_paper_count > 0:
                 print(f"    - Found {monthly_paper_count} papers this month.")

        except UnexpectedEmptyPageError:
            total_results_for_year += monthly_paper_count
            print(f"    - Found {monthly_paper_count} papers this month (API returned empty page).")
        except Exception as e:
            print(f"    - An unexpected error occurred in {year}-{month_str}: {e}")

    # After all months are done, report and store the yearly total
    print(f"Finished year {year}. Total papers found: {total_results_for_year}")
    
    year_data = {"year": year, "total_publications": total_results_for_year}
    year_data.update(keyword_counts_for_year)
    trends_list.append(year_data)


# Save the final data...
if trends_list:
    df_trends = pd.DataFrame(trends_list)
    output_path = Path(__file__).parent.parent / "data" / "raw" / "arxiv_trends_by_month.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_trends.to_csv(output_path, index=False)
    print(f"\nData successfully saved to: {output_path.resolve()}")
else:
    print("\nCould not collect any data, no file was created.")









    

    
