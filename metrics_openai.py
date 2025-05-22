from openai import OpenAI
import os
import ast

client = OpenAI(
    api_key="sk-schoolaiassistant-IJAus8rOlO5f3hnrBcyuT3BlbkFJ60gsZPoeRzVR0bwKuABN"
)


def extract_metrics_with_openai(text, quarter="Q1FY24"):
    prompt = f"""
You are a financial data extraction assistant.

From the following text, extract the key financial metrics for **Q1 FY24**, as published in the investor presentation.

Please extract the following **in full precision** exactly as found in the text:

### Primary Financial Metrics
1. Revenue from Operations (₹ Cr)
2. EBITDA (₹ Cr)
3. EBITDA Margin (%)
4. PAT (Profit After Tax, ₹ Cr)
5. PAT Margin (%)
6. Free Cash Flow (₹ Cr)
7. Total Income (₹ Cr)
8. Cash and Cash Equivalents (₹ Cr)

### Additional Metrics (if available)
9. EBITDA excluding IPO Expense (₹ Cr)
10. EBITDA Margin excluding IPO Expense (%)
11. PAT excluding IPO expense and Deferred Tax (₹ Cr)
12. PAT Margin excluding IPO expense and Deferred Tax (%)

### Year-over-Year (YoY) Comparisons (if mentioned)
13. Revenue YoY Change (%)
14. PAT YoY Change (%)
15. Free Cash Flow YoY Change (%)
16. Total Income YoY Change (%)

### Output Format
Return a Python list of tuples in this exact format:
[("Q1FY24", "Metric Name", "Value in original format")]

If a value is not available, use "N/A" in the third field.

Do NOT include any explanations, headers, markdown, or comments. Output ONLY the list of tuples. This will be parsed directly by a program.

Here is the financial text to extract from:
{text[:20000]}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You're a financial data extraction assistant.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    content = response.choices[0].message.content.strip()
    print("GPT Output:\n", content)  

    try:
        data = ast.literal_eval(content)
        return data
    except Exception as e:
        print("GPT output could not be parsed:", e)
        return []
