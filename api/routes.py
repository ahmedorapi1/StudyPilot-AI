from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from graph.flow import build_graph

router = APIRouter()
engine = build_graph()


class Request(BaseModel):
    student_id: str
    topic: str
    answer: str | None = None
    level: str = "medium"
    max_attempts: int = 5
    target_score: int = 80


class Response(BaseModel):
    student_id: str
    topic: str
    level: str
    attempt: int
    score: int | None = None
    feedback: str | None = None
    explanation: str | None = None
    question: str | None = None


@router.post("/study", response_model=Response)
def study(request: Request):
    try:
        state = engine.invoke(request.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return Response(**{
        "student_id": state.get("student_id"),
        "topic": state.get("topic"),
        "level": state.get("level", "medium"),
        "attempt": state.get("attempt", 0),
        "score": state.get("score"),
        "feedback": state.get("feedback"),
        "explanation": state.get("explanation"),
        "question": state.get("question"),
    })
