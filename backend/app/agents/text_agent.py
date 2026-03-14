from app.agents.base_agent import BaseAgent


class TextAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("text-agent", "Handles text tasks")

    def run(self, task):
        return str(task).upper()

