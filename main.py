from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from api.routes import router

app = FastAPI(
    title="StudyPilot AI",
    description="AI-powered study assistant",
    version="1.0.0"
)
app.include_router(router)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
