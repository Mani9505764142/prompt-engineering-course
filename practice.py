from helper import get_completion

prompt = """
Translate this sentence into three languages:1.Telugu 2. Tamil 3 . Hindi

Prompt engineering helps us write clear instructions for AI models.
"""

response = get_completion(prompt)
print(response)