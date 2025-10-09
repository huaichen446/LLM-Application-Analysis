from pathlib import Path
import pandas as pd
from datasets import load_dataset

# -------------------------------
# Parameter Settings
# -------------------------------
TARGET_N = 2000
OUTPUT_FILE = "realm_reddit_sample_raw.csv"

# -------------------------------
# 1. Load REALM dataset
# -------------------------------
print("Loading REALM dataset...")
ds = load_dataset("kkChimmy/REALM", split="train")
df = ds.to_pandas()
print(f"Total Data Volume: {len(df)} ")

# -------------------------------
# 2. Filter Reddit data
# -------------------------------
df_reddit = df[df["source"].str.lower() == "reddit"].copy()
print(f"Reddit Subset size: {len(df_reddit)} ")

# -------------------------------
# 3.Randomly sample 2,000 items
# -------------------------------
if len(df_reddit) < TARGET_N:
    raise RuntimeError("Reddit Insufficient data: less than 2000 entries")

sampled_df = df_reddit.sample(n=TARGET_N, random_state=42).reset_index(drop=True)
print(f"Sampling completed, number of samples: {len(sampled_df)} ")


output_path = Path(__file__).parent.parent / "data" / "raw" / OUTPUT_FILE
output_path.parent.mkdir(parents=True, exist_ok=True)

sampled_df.to_csv(output_path, index=False, encoding="utf-8")
print(f" The sample CSV file has been exported to: {output_path}")
