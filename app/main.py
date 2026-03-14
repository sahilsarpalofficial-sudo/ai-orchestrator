from fastapi import FastAPI
import os


app = FastAPI(title="ai-orchestrator")


@app.get("/healthz")
def health_check():
    return {
        "status": "ok",
        "database_url_set": bool(os.getenv("DATABASE_URL")),
    }

