# ai-orchestrator

## Overview

`ai-orchestrator` is a backend-first project for building an agent orchestration engine.  
Today’s scope is to provide a **professional foundation**, a **clean repo**, and a **running backend** – not the full agent engine yet.

## Tech Stack (Backend)

- **Python**: 3.11 (via Docker)
- **Framework**: FastAPI
- **Database**: Postgres (via Docker)
- **Containerization**: Docker + Docker Compose

## Repository Structure

```text
.
├── backend
│   ├── app
│   │   ├── main.py          # FastAPI entrypoint with / health route
│   │   ├── config.py        # Settings / environment config (env-file based)
│   │   ├── core/            # Core engine primitives (empty for now)
│   │   ├── agents/          # Agent definitions (empty for now)
│   │   ├── tools/           # Tool integrations (empty for now)
│   │   ├── memory/          # Memory layer (empty for now)
│   │   └── orchestration/   # Orchestration logic (empty for now)
│   ├── Dockerfile           # Python 3.11 + FastAPI image
│   └── requirements.txt     # Backend Python dependencies
├── docker-compose.yml       # Backend + Postgres dev stack
├── frontend/                # Reserved for future UI
├── docs/                    # Documentation space
└── README.md
```

## Backend Python Environment

### Inside Docker (recommended)

The primary dev environment is Docker-based. You do **not** need Python 3.11 or Postgres installed locally.

Dependencies (declared in `backend/requirements.txt`):

- `fastapi`
- `uvicorn[standard]`
- `pydantic`
- `python-dotenv`
- `sqlalchemy`
- `psycopg2-binary`

### Optional local virtualenv (host)

If you want to run the backend directly on your machine:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open `http://localhost:8000/` to hit the health endpoint.

## Running the Stack with Docker

Prerequisites:

- Docker Desktop (or Docker Engine)
- Docker Compose v2 (bundled with recent Docker Desktop)

From the repo root:

```bash
docker compose up --build
```

This will:

- Start **Postgres** as `db` service (`postgres:16-alpine`)
- Build and start the **FastAPI backend** as `web` service from `backend/Dockerfile`
- Expose the backend on `http://localhost:8000`

Health check:

```bash
curl http://localhost:8000/
# {"status": "AgentOS running"}
```

## What Is Implemented So Far (Day 1)

- **Project setup**
  - Git repository initialized and connected to GitHub.
  - Clear backend-first structure under `backend/app`.
  - Placeholders created for `core`, `agents`, `tools`, `memory`, and `orchestration` packages.

- **Backend service**
  - Minimal FastAPI app in `backend/app/main.py`:
    - `GET /` → `{"status": "AgentOS running"}`
  - Config module in `backend/app/config.py` using Pydantic settings with `.env` support.

- **Infrastructure**
  - `backend/Dockerfile` with:
    - Base image `python:3.11-slim`
    - System deps for Postgres driver
    - Install of `backend/requirements.txt`
    - Uvicorn command to run FastAPI with reload.
  - `docker-compose.yml` wiring:
    - `db` → Postgres database with dedicated user, password, and DB.
    - `web` → FastAPI backend, depends on `db` and exposes port `8000`.

## Next Steps (Not Done Yet)

These are **explicitly not implemented yet**, but the structure is ready:

- Agent engine and orchestration workflows.
- Tool integrations and memory backends.
- Frontend UI in `/frontend`.

The current goal is a solid, production-ready foundation with a clean layout and a running backend service.
