from fastapi import APIRouter

from app.orchestration.runner import Runner
from app.schemas.task import TaskRequest


router = APIRouter()
runner = Runner()


@router.post("/run-task")
def run_task(payload: TaskRequest):
    return runner.execute(payload.task)

