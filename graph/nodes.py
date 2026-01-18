import json
from graph.state import State
from chains.teacher_chain import teacher_chain
from chains.practise_chain import practise_chain
from chains.grader_chain import grader_chain


def explain_node(state: State):
    state["explanation"] = teacher_chain.invoke({"topic": state["topic"]})
    return state


def practise_node(state: State):
    state["question"] = practise_chain.invoke({
        "topic": state["topic"],
        "level": state.get("level", "medium")
    })
    return state


def grade_node(state: State):
    raw = grader_chain.invoke({
        "question": state["question"],
        "answer": state["answer"]
    })

    try:
        data = json.loads(raw)
    except:
        state["score"] = 0
        state["feedback"] = "Invalid answer format, please try again."
        return state

    state["score"] = data.get("score", 0)
    state["feedback"] = data.get("feedback", "")
    return state
