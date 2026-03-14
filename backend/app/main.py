from fastapi import FastAPI


app = FastAPI(title="AgentOS Backend")


@app.get("/")
def health():
    return {"status": "AgentOS running"}

