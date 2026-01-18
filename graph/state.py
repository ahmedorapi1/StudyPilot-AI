from typing import TypedDict, Optional

class State(TypedDict):
    student_id: str
    topic: str
    question: Optional[str]
    answer: Optional[str]
    explanation: Optional[str]
    score: Optional[int]
    feedback: Optional[str]
