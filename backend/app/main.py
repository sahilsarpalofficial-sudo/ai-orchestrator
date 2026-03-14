from fastapi import FastAPI

from app.api.routes import router as api_router


app = FastAPI(title="AgentOS Backend")


@app.get("/")
def health():
    return {"status": "AgentOS running"}


app.include_router(api_router)

