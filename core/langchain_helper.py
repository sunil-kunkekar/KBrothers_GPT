# cpore/langchain_helper.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os
from .prompts import PROMPT_TEMPLATES



def generate_response(prompt_text, prompt_type="qa"):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-002",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7
    )
    prompt_template = PROMPT_TEMPLATES.get(prompt_type)
    if not prompt_template:
        return "Invalid prompt type."

    chain = prompt_template | llm
    result = chain.invoke({"input": prompt_text})
    return result.content if hasattr(result, "content") else result

# def generate_answer_from_prompt(prompt_text):
#     template = """
#     You are an expert assistant. Provide a clear, detailed, and well-explained answer to the question below. 
#     Your answer should include examples, background information, and be beginner-friendly.

#     Question: {prompt}

#     Answer:
#     """

#     prompt = PromptTemplate.from_template(template)

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-1.5-flash-002",
#         google_api_key=os.getenv("GOOGLE_API_KEY"),
#         temperature=0.7
#     )

#     # Combine prompt and llm using invoke (modern LangChain syntax)
#     chain = prompt | llm
#     result = chain.invoke({"prompt": prompt_text})
#     return result.content if hasattr(result, "content") else result
