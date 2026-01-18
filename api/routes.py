from fastapi import APIRouter
from graph.flow import build_graph

router = APIRouter()
app = build_graph()

@router.post("/study")
def study(data: dict):
    return app.invoke({
        "student_id": data.get("student_id", "0"),
        "topic": data["topic"],
        "answer": data.get("answer"),
        "level": data.get("level", "medium")
    })
