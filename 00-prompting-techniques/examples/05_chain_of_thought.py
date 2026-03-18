import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
You are a business analyst.

Solve the problem step by step.

Return output in this exact format:

Revenue: ₹<value>
Cost: ₹<value>
Profit: ₹<value>
Suggestion: <one line>

No extra explanation.

Problem:
A small business sells 120 products per month at ₹500 each.
Its monthly marketing spend is ₹12,000 and operational costs are ₹25,000.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)