import json
from graph.state import State
from chains.teacher_chain import run_teacher
from chains.practice_chain import run_practice
from chains.grader_chain import run_grader


def explain_node(state: State):
    state["explanation"] = run_teacher(state["topic"])
    return state


def practice_node(state: State):
    state.setdefault("level", "medium")
    state.setdefault("attempt", 0)
    state.setdefault("max_attempts", 5)
    state.setdefault("target_score", 80)

    state["question"] = run_practice(
        topic=state["topic"],
        level=state["level"]
    )
    return state


def grade_node(state: State) -> State:
    state["attempt"] = state.get("attempt", 0) + 1

    raw = run_grader(
        topic=state["topic"],
        question=state.get("question", ""),
        answer=state.get("answer", "")
    )

    try:
        data = json.loads(raw)
        state["score"] = int(data.get("score", 0))
        state["feedback"] = data.get("feedback", "")
    except Exception:
        state["score"] = 0
        state["feedback"] = "Invalid grading response."

    return state
