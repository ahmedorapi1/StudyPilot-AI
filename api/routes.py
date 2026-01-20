from fastapi import APIRouter, HTTPException
import json
from api.schemas import (
    StudyRequest,
    PracticeRequest,
    GradeRequest,
    StudyResponse,
    GradeResponse,
    PracticeResponse
)
from chains.teacher_chain import run_teacher
from chains.practice_chain import run_practice
from chains.grader_chain import run_grader


router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "StudyPilot AI is running"}


@router.post("/study", response_model=StudyResponse)
def study(req: StudyRequest):

    if not req.topic:
        raise HTTPException(status_code=400, detail="Topic is required")

    explanation = run_teacher(req.topic)

    return {
        "explanation": explanation,
    }


@router.post("/practice", response_model=PracticeResponse)
def practice(req: PracticeRequest):

    if not req.topic:
        raise HTTPException(status_code=400, detail="topic is required")

    if not req.level:
        questions = run_practice(req.topic)
    else:
        questions = run_practice(req.topic, req.level)
    return {
        "question": questions
    }


@router.post("/grading", response_model=GradeResponse)
def grading(req: GradeRequest):
    response = run_grader(req.topic, req.question, req.answer)
    return json.loads(response)

