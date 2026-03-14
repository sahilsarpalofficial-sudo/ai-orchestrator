from typing import List

from pydantic import BaseModel


class TaskRequest(BaseModel):
    task: List[float]


class TaskResponse(BaseModel):
    result: float

