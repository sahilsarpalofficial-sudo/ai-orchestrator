from .base_tool import BaseTool


class CalculatorTool(BaseTool):
    def __init__(self) -> None:
        super().__init__("calculator")

    def execute(self, input_data):
        return sum(input_data)

