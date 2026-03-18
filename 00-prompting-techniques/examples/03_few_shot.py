import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
You are a sentiment classification assistant.

Classify the sentiment as one of:
Positive, Negative, or Neutral.

Rules:
- Return ONLY one word
- No explanation
- Follow the exact format

Examples:
Sentence: The product quality is excellent and delivery was fast.
Sentiment: Positive

Sentence: The app keeps crashing every time I open it.
Sentiment: Negative

Sentence: The package arrived yesterday afternoon.
Sentiment: Neutral

Now classify:

Sentence: The course content is useful, but the audio quality is poor.
Sentiment:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)