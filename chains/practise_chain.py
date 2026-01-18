from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm import get_llm
from core import project_path as pth

llm = get_llm()


practise_prompt = PromptTemplate(
    input_variables=["topic", "level"],
    template=pth.join("prompts/practise_prompt.txt").read_text(encoding="utf-8")
)

practise_chain = practise_prompt | llm | StrOutputParser()

