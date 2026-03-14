from typing import List, Union

from pydantic import BaseModel


class TaskRequest(BaseModel):
    task: Union[str, List[float]]



