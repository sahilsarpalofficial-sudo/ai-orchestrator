from app.agents.math_agent import MathAgent
from app.agents.text_agent import TextAgent


class Router:
    def select_agent(self, task):
        if isinstance(task, list):
            return MathAgent()
        if isinstance(task, str):
            return TextAgent()
        return None

