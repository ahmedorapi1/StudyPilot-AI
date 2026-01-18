from typing import TypedDict, Optional

class State(TypedDict, total=False):
    # Inputs
    student_id: str
    topic: str
    answer: Optional[str]

    # Runtime / control
    level: str              # "easy" | "medium" | "hard"
    attempt: int            # current attempt count
    max_attempts: int       # stop after this many attempts
    target_score: int       # end if score >= target_score

    # Outputs
    question: Optional[str]
    explanation: Optional[str]
    score: Optional[int]
    feedback: Optional[str]
