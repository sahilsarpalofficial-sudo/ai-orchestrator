# Architecture v1

## Goal

Provide a minimal but serious AI orchestration skeleton that cleanly separates:

- **Agents** – who does the work
- **Tools** – how concrete actions are executed
- **Orchestration** – how tasks are routed and executed
- **Schemas** – how data flows between layers
- **API** – how external callers interact with the system

This structure is intentionally simple but mirrors how modern agent frameworks model:

> Instruction + Context + Tools + Model

## High-Level Layout

```text
backend/
  app/
    main.py           # FastAPI app, wires routers
    config.py         # Settings and environment
    api/
      routes.py       # HTTP endpoints (e.g. /run-task)
    agents/
      base_agent.py   # Base abstraction for agents
      math_agent.py   # Example concrete agent
    tools/
      base_tool.py    # Base abstraction for tools
      calculator_tool.py  # Example concrete tool
    orchestration/
      runner.py       # Orchestrator that owns agents and runs tasks
    schemas/
      task.py         # Request / response contracts
    core/
      logger.py       # Centralized logging setup
```

## Data Flow (v1)

1. **Client → API**
   - Client calls `POST /run-task` with JSON payload:
     - `{"task": [5, 10]}`
   - FastAPI validates this into a `TaskRequest` schema.

2. **API → Orchestration**
   - The route calls `Runner.execute(task)`.
   - `Runner` is responsible for selecting and invoking the appropriate agent.

3. **Orchestration → Agent**
   - `Runner` currently uses a single `MathAgent` instance.
   - `MathAgent` receives the task (a list of numbers).

4. **Agent → Tool**
   - `MathAgent` delegates concrete work to `CalculatorTool`.
   - `CalculatorTool.execute(input_data)` performs the arithmetic.

5. **Back to Client**
   - `Runner` returns the tool result.
   - API wraps it into a `TaskResponse` schema:
     - `{"result": 15}`

## Extensibility Thoughts

- **More Agents**
  - Add additional agent classes under `app/agents/`.
  - `Runner` can dispatch based on task type, metadata, or routing rules.

- **More Tools**
  - Each tool lives in `app/tools/` and inherits from `BaseTool`.
  - Agents can be configured with multiple tools.

- **Richer Schemas**
  - `schemas/task.py` can evolve to include:
    - `task_type`, `context`, `metadata`, `tool_preferences`, etc.

- **LLM Integration**
  - Future layers can plug LLM calls into agents or tools without changing:
    - API contracts
    - Orchestrator semantics

This v1 focuses on **clear separation of roles** and **testable orchestration** before introducing any model or vendor-specific integrations.

