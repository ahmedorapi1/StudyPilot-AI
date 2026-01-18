from langgraph.graph import StateGraph, END
from graph.state import State
from graph.nodes import explain_node, practise_node, grade_node


def route_after_grade(state: State):
    score = int(state.get("score") or 0)
    attempt = int(state.get("attempt") or 0)
    max_attempts = int(state.get("max_attempts") or 5)
    target_score = int(state.get("target_score") or 80)

    if score >= target_score or attempt >= max_attempts:
        return END

    if score < 50:
        return "explain"

    return "practise"


def build_graph():
    graph = StateGraph(State)

    graph.add_node("explain", explain_node)
    graph.add_node("practise", practise_node)
    graph.add_node("grade", grade_node)

    graph.set_entry_point("explain")
    graph.add_edge("explain", "practise")
    graph.add_edge("practise", "grade")

    # Feedback loop
    graph.add_conditional_edges(
        "grade",
        route_after_grade,
        {
            "explain": "explain",
            "practise": "practise",
            END: END
        }
    )

    return graph.compile()
