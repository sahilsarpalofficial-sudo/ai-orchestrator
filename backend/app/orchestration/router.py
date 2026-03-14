from app.agents.llm_agent import LLMAgent
from app.agents.math_agent import MathAgent


class Router:
    def select_agent(self, task):
        if isinstance(task, list):
            return MathAgent()
        if isinstance(task, str):
            return LLMAgent()
        return None

