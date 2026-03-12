import os
import json
from dotenv import load_dotenv
from groq import Groq

MODEL = "llama-3.1-8b-instant"
load_dotenv()


def extract_keywords_llm(resume_text: str):

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("Please set GROQ_API_KEY environment variable.")

    client = Groq(api_key=api_key)

    prompt = f"""
Extract the most important job search keywords from this resume.

Return ONLY a JSON list of keywords.

Example:
["machine learning","python","data science","nlp"]

Resume:
{resume_text[:6000]}
"""

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    response = completion.choices[0].message.content.strip()

    try:
        keywords = json.loads(response)
    except Exception:
        keywords = []

    return keywords