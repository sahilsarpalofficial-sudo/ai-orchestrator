import json
import time
import uuid
from typing import Any, Dict, List


class ExecutionLogger:
    def start_run(self) -> Dict[str, Any]:
        run_data: Dict[str, Any] = {
            "run_id": str(uuid.uuid4()),
            "start_time": time.time(),
            "trace": [],
        }
        return run_data

    def add_trace(self, run_data: Dict[str, Any], message: str) -> None:
        trace: List[str] = run_data.setdefault("trace", [])
        trace.append(message)

    def end_run(
        self,
        run_data: Dict[str, Any],
        agent_name: str,
        task: Any,
        result: Any,
    ) -> Dict[str, Any]:
        latency_ms = round((time.time() - run_data["start_time"]) * 1000, 2)

        payload = {
            "run_id": run_data["run_id"],
            "agent": agent_name,
            "task": task,
            "result": result,
            "latency_ms": latency_ms,
            "trace": run_data.get("trace", []),
        }

        # Structured console trace for development
        print(f"[TRACE] {json.dumps(payload, default=str)}")

        return payload

