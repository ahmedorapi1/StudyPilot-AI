from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="StudyPilot AI",
    description="AI-powered study assistant",
    version="1.0.0"
)

app.include_router(router)
