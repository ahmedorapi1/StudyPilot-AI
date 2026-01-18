from langgraph.graph import StateGraph
from graph.state import State
from graph.nodes import explain_node, practise_node, grade_node


def build_graph():
    graph = StateGraph(State)

    graph.add_node("explain", explain_node)
    graph.add_node("practise", practise_node)
    graph.add_node("grade", grade_node)

    graph.set_entry_point("explain")
    graph.add_edge("explain", "practise")
    graph.add_edge("practise", "grade")

    return graph.compile()
