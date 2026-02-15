import os
from groq import Groq

# Paste your Groq API key here temporarily
client = Groq(api_key="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")

topic = input("Enter a topic: ")

prompt = f"""
Write a YouTube video script about: {topic}

Make it:
- Engaging
- 1-2 minutes long
- Clear introduction
- 5 key points
- Strong conclusion
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

script = response.choices[0].message.content

print("\nGenerated Script:\n")
print(script)

with open("script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("\nScript saved as script.txt")
