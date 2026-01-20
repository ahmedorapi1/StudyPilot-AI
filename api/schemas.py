from pydantic import BaseModel
from typing import Optional


class StudyRequest(BaseModel):
    student_id: str
    topic: str
    level: str


class PracticeRequest(BaseModel):
    topic: str
    level: Optional[str] = None


class PracticeResponse(BaseModel):
    question: str


class GradeRequest(BaseModel):
    topic: str
    question: str
    answer: str


class StudyResponse(BaseModel):
    explanation: str


class GradeResponse(BaseModel):
    score: int
    feedback: str
