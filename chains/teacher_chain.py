from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm import get_llm

llm = get_llm

teacher_prompt = PromptTemplate(
    input_variables=["topic"],
    template=open("C:/Users/hp/Desktop/Study Pilot AI/prompts/teacher_prompt.txt").read()
)

teacher_chain = teacher_prompt | llm | StrOutputParser()

