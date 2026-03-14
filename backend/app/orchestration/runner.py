from app.orchestration.router import Router


class Runner:
    def __init__(self) -> None:
        self.router = Router()

    def execute(self, task):
        agent = self.router.select_agent(task)
        if not agent:
            return {"error": "No suitable agent found"}

        result = agent.run(task)

        return {
            "agent": agent.name,
            "result": result,
        }

