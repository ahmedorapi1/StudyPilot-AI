import json
from graph.state import State
from chains.teacher_chain import run_teacher
from chains.practise_chain import run_practise
from chains.grader_chain import run_grader


def explain_node(state: State):
    state["explanation"] = run_teacher({"topic": state["topic"]})
    return state


def practise_node(state: State):
    state.setdefault("level", "medium")
    state.setdefault("attempt", 0)
    state.setdefault("max_attempts", 5)
    state.setdefault("target_score", 80)

    state["question"] = run_practise({
        "topic": state["topic"],
        "level": state["level"],
    })
    return state


def grade_node(state: State):
    state.setdefault("attempt", 0)
    state.setdefault("max_attempts", 5)
    state.setdefault("target_score", 80)

    state["attempt"] = int(state["attempt"]) + 1

    raw = run_grader({
        "topic": state.get("topic",""),
        "question": state.get("question", ""),
        "answer": state.get("answer", "")
    })

    try:
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError("Invalid JSON structure")
    except Exception:
        state["score"] = 0
        state["feedback"] = "Invalid answer format. Please return JSON only."
        return state

    state["score"] = int(data.get("score", 0))
    state["feedback"] = data.get("feedback", "")
    return state
