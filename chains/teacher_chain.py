from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm import get_llm
from core import project_path as pth

llm = get_llm()

teacher_prompt = PromptTemplate(
    input_variables=["topic"],
    template=pth.join("prompts/teacher_prompt.txt").read_text(encoding="utf-8")
)

teacher_chain = teacher_prompt | llm | StrOutputParser()

