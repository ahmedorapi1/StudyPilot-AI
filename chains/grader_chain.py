from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm import get_llm

llm = get_llm


grader_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template=open("C:/Users/hp/Desktop/Study Pilot AI/prompts/grader_prompt.txt").read()
)

grader_chain = grader_prompt | llm | StrOutputParser()
