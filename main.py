from fastapi import FastAPI
from routers.program_router import router as program_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="🏋️ Program Builder API",
    description="AI-powered backend service for generating personalized fitness programs using Claude and Firebase",
    version="1.0.0"
)

app.include_router(program_router, prefix="/program")

@app.get("/")
def root():
    return {"message": "Claude + LangChain is running"}
