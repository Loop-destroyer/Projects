import pdfplumber
import pandas as pd
import re

def extract_cutoff_data(pdf_paths):
    cutoff_data = []

    for path in pdf_paths:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()

                # Regex to identify cutoff lines (e.g., "Category Percentile Rank")
                matches = re.findall(r"([A-Za-z0-9/\-]+)\s+(\d{1,3}\.\d{2,6})\s+(\d+)", text)

                for match in matches:
                    category, percentile, rank = match
                    cutoff_data.append({
                        "PDF": path,
                        "Category": category,
                        "Percentile": float(percentile),
                        "Rank": int(rank),
                    })

    return pd.DataFrame(cutoff_data)

def analyze_cutoffs(cutoff_df):
    # Group by category and summarize stats
    summary = cutoff_df.groupby("Category").agg({
        "Percentile": ["mean", "max", "min"],
        "Rank": ["mean", "max", "min"]
    }).reset_index()
    summary.columns = ["Category", "Avg Percentile", "Max Percentile", "Min Percentile",
                       "Avg Rank", "Max Rank", "Min Rank"]
    return summary

if __name__ == "__main__":
    # Paths to your PDF files
    pdf_files = ["230601_Cutoff-2022-for-information.pdf", "VJTI-Cut-offs-2023-24.pdf"]

    # Extract cutoff data from PDFs
    cutoff_df = extract_cutoff_data(pdf_files)

    # Save raw data to CSV for review
    cutoff_df.to_csv("cutoff_data.csv", index=False)

    # Analyze and save summary
    summary = analyze_cutoffs(cutoff_df)
    summary.to_csv("cutoff_summary.csv", index=False)

    print("Cutoff analysis complete. Results saved to cutoff_data.csv and cutoff_summary.csv.")
