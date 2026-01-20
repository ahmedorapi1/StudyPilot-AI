from fastapi import APIRouter
from graph.flow import build_graph

router = APIRouter()
graph_app = build_graph()


@router.post("/learn")
def learn(payload: dict):

    initial_state = {
        "topic": payload.get("topic"),
        "answer": payload.get("answer", ""),
        "level": payload.get("level", "medium"),
        "attempt": payload.get("attempt", 0),
        "max_attempts": 5,
        "target_score": 80
    }

    final_state = graph_app.invoke(initial_state)

    return {
        "explanation": final_state.get("explanation"),
        "question": final_state.get("question"),
        "score": final_state.get("score"),
        "feedback": final_state.get("feedback"),
        "attempt": final_state.get("attempt")
    }
