from app.agents.math_agent import MathAgent


class Runner:
    def __init__(self) -> None:
        self.agent = MathAgent()

    def execute(self, task):
        return self.agent.run(task)

