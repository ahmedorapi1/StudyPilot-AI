from langchain_core.prompts import PromptTemplate
from core.llm import get_llm
from core import project_path as pth
from RAG.retriver import retrive_questions

llm = get_llm()


grader_prompt = PromptTemplate(
    input_variables=["context", "question", "answer"],
    template=pth.join("prompts/grader_prompt.txt").read_text(encoding="utf-8"))

def run_grader(topic, question, answer):
    context = retrive_questions(topic)
    return llm.invoke(grader_prompt.format(context=context, question=question, answer=answer))
