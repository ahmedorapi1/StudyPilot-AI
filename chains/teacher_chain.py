from langchain_core.prompts import PromptTemplate
from core.llm import get_llm
from core import project_path as pth
from rag.retriever import retrive_theory


llm = get_llm()

teacher_prompt = PromptTemplate(
    input_variables=["context", "topic"],
    template=pth.join("prompts/teacher_prompt.txt").read_text(encoding="utf-8")
)


def run_teacher(topic):
    context = retrive_theory(topic)
    return llm.invoke(teacher_prompt.format(context=context, topic=topic))
