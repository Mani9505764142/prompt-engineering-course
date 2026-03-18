# 🧠 Prompt Engineering – Practical Implementation

A hands-on implementation of core prompt engineering techniques using Python and the Gemini AI API.

---

## 📚 Topics Covered

| Technique | File | Description |
|---|---|---|
| Zero-shot Prompting | `01_zero_shot.py` | Querying the model with no examples |
| One-shot Prompting | `02_one_shot.py` | Guiding output with a single example |
| Few-shot Prompting | `03_few_shot.py` | Improving consistency with 2–5 examples |
| Multi-shot Prompting | `04_multi_shot.py` | Robust output control with many examples |
| Chain-of-Thought | `05_chain_of_thought.py` | Step-by-step reasoning for complex tasks |

---

## 💡 What I Learned

- How to control AI outputs using structured prompts
- How to improve response consistency using few-shot and multi-shot techniques
- How to apply chain-of-thought reasoning for multi-step problem solving
- How to convert prompt patterns into real-world use cases
- How prompt design affects tone, format, and accuracy

---

## 🗂️ Project Structure

```
prompt-engineering/
│
├── 01_zero_shot.py         # No examples — raw instruction only
├── 02_one_shot.py          # Single example to guide the model
├── 03_few_shot.py          # 2–5 examples for consistent outputs
├── 04_multi_shot.py        # Multiple examples for complex tasks
├── 05_chain_of_thought.py  # Step-by-step reasoning prompts
│
├── results/                # Sample outputs and comparisons (coming soon)
└── README.md
```

---

## ⚙️ Setup & Usage

### Prerequisites
- Python 3.8+
- A Google Gemini API key → [Get one here](https://aistudio.google.com/app/apikey)

### Installation

```bash
git clone https://github.com/your-username/prompt-engineering
cd prompt-engineering
pip install google-generativeai
```

### Configuration

Set your API key as an environment variable:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

### Run any example

```bash
python 01_zero_shot.py
python 05_chain_of_thought.py
```

---

## 🔥 Next Steps

- [ ] `06_comparison.py` — Side-by-side output comparison across all techniques
- [ ] Role prompting — Persona-based prompts for tone and expertise control
- [ ] JSON output prompting — Structured, parseable AI responses
- [ ] Prompt chaining — Breaking complex tasks into sequential prompts
- [ ] **AI Blog App** — Real-world project applying these techniques
- [ ] **ATS Resume Analyzer** — Role + few-shot + structured output in action

---

## 🧪 Techniques at a Glance

```
Zero-shot   →  "Classify this text as positive or negative."
One-shot    →  "Here's one example. Now do the same for this."
Few-shot    →  "Here are 3 examples. Follow the same pattern."
Multi-shot  →  "Here are 10 examples. Be highly consistent."
CoT         →  "Think step by step before giving your final answer."
```

---

## 📌 Resources

- [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [Google AI Studio](https://aistudio.google.com)
- [Gemini Prompt Engineering Guide](https://ai.google.dev/gemini-api/docs/prompting-intro)

---

*Built as part of a structured prompt engineering learning path.*
