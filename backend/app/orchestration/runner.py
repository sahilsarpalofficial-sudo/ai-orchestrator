from app.core.logger import ExecutionLogger
from app.orchestration.router import Router


class Runner:
    def __init__(self) -> None:
        self.router = Router()
        self.logger = ExecutionLogger()

    def execute(self, task):
        run_data = self.logger.start_run()
        self.logger.add_trace(run_data, "runner:start")

        agent = self.router.select_agent(task)

        if not agent:
            self.logger.add_trace(run_data, "router:no-agent")
            return {
                "error": "No suitable agent",
                "trace": run_data.get("trace", []),
            }

        self.logger.add_trace(run_data, f"router:selected {agent.name}")

        try:
            result = agent.run(task)
            self.logger.add_trace(run_data, f"agent:{agent.name} completed")
        except Exception as exc:  # noqa: BLE001
            self.logger.add_trace(run_data, f"error:{exc}")
            return self.logger.end_run(
                run_data,
                agent.name,
                task,
                f"error:{exc}",
            )

        return self.logger.end_run(
            run_data,
            agent.name,
            task,
            result,
        )

