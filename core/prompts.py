from langchain.prompts import PromptTemplate

PROMPT_TEMPLATES = {
    "qa": PromptTemplate.from_template(
        """You are a helpful assistant. Answer this question in detail:
        Question: {input}
        Answer:"""
    ),
    "summarize": PromptTemplate.from_template(
        """Summarize the following text in simple language:
        {input}
        Summary:"""
    ),
    "explain_code": PromptTemplate.from_template(
        """Explain what the following Python code does:
        {input}
        Explanation:"""
    )
}
