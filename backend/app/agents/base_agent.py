class BaseAgent:
    def __init__(self, name: str, instruction: str) -> None:
        self.name = name
        self.instruction = instruction

    def run(self, task: str):
        raise NotImplementedError

