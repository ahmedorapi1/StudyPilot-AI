from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm import get_llm
from core import project_path as pth

llm = get_llm()


grader_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template=pth.join("prompts/grader_prompt.txt").read_text(encoding="utf-8"))

grader_chain = grader_prompt | llm | StrOutputParser()
