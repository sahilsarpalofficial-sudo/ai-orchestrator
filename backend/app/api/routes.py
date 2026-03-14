from fastapi import APIRouter

from app.orchestration.runner import Runner
from app.schemas.task import TaskRequest, TaskResponse


router = APIRouter()
runner = Runner()


@router.post("/run-task", response_model=TaskResponse)
def run_task(payload: TaskRequest) -> TaskResponse:
    result = runner.execute(payload.task)
    return TaskResponse(result=result)

