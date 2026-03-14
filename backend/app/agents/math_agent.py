from app.agents.base_agent import BaseAgent
from app.tools.calculator_tool import CalculatorTool


class MathAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("math-agent", "Handles arithmetic tasks")
        self.tool = CalculatorTool()

    def run(self, task):
        return self.tool.execute(task)

