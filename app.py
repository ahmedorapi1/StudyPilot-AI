from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="StudyPilot AI")
app.include_router(router)
