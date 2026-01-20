from langchain_core.prompts import PromptTemplate
from core.llm import get_llm
from core import project_path as pth
from RAG.retriver import retrive_questions

llm = get_llm()


practice_prompt = PromptTemplate(
    input_variables=["context", "topic", "level"],
    template=pth.join("prompts/practice_prompt.txt").read_text(encoding="utf-8")
)

def run_practice(topic, level='medium'):
    context = retrive_questions(topic)
    return llm.invoke(practice_prompt.format(context=context, topic=topic, level=level))
