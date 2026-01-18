from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm import get_llm

llm = get_llm


practise_prompt = PromptTemplate(
    input_variables=["topic", "level"],
    template=open("C:/Users/hp/Desktop/Study Pilot AI/prompts/practise_prompt.txt").read()
)

practise_chain = practise_prompt | llm | StrOutputParser()

