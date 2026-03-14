from app.agents.base_agent import BaseAgent
from app.providers.openai_provider import OpenAIProvider


class LLMAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("llm-agent", "Handles language tasks")
        self.provider = OpenAIProvider()

    def run(self, task):
        return self.provider.generate(str(task))

