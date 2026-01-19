from langchain_core.prompts import PromptTemplate
from core.llm import get_llm
from core import project_path as pth
from rag.retriver import retrive_questions

llm = get_llm()


practise_prompt = PromptTemplate(
    input_variables=["context", "topic", "level"],
    template=pth.join("prompts/practise_prompt.txt").read_text(encoding="utf-8")
)

def run_practise(topic, level='medium'):
    context = retrive_questions(topic)
    return llm.invoke(practise_prompt.format(context=context, topic=topic, level=level))
