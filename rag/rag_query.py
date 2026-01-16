from rag.retriever import search
from llm.safe_generate import safe_generate

def answer(question):
    context = "\n".join(search(question))

    prompt = f"""
You are an expert on the ERPNext codebase.

## Context
{context}

## Question
{question}

## Instructions
- Base your answer on the provided context
"""

    return safe_generate(prompt)
