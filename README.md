# ai-tax-desk-api

Backend for an AI front desk for Brazilian accounting firms. It answers MEI and Simples Nacional
questions from official sources, cites where each answer comes from, and hands the conversation
to the accountant when the sources don't support an answer.

> **Status: early development.** This README describes the target design; the service does not
> answer questions yet.

The web client lives in a separate repository, `ai-tax-desk-web`, and talks to this API only
through its OpenAPI contract.

## What it will do

- **Answer from official sources, with citations:** each answer names the document, the article or
  official question, and the date it took effect.
- **Abstain instead of guessing:** when the retrieved sources don't support an answer, it says so
  and hands off to the accountant.
- **Take actions with confirmation:** look up a client's pending obligations and book a meeting
  with the accountant. The model proposes; nothing is written until it is confirmed.

It is a triage and front-desk tool, **not tax advice**.

## Architecture

A modular monolith with a hexagonal structure inside each module. One Python package runs as
several processes: the HTTP API, a background worker and MCP tool servers.

| Module | Responsibility |
|---|---|
| `knowledge` | ingestion of official sources, hybrid search, citations, effective dates |
| `assistant` | LangGraph flow: triage, question, action, hand-off |
| `scheduling` | the accountant's calendar |
| `clients` | client obligations (fictional data) |
| `shared` | configuration, LLM client, audit |
| `entrypoints` | FastAPI routes, Celery worker, MCP servers |

**Planned stack:** FastAPI, Pydantic, LangGraph, Celery + Redis, PostgreSQL + pgvector, pytest.

## Running locally

Requires [uv](https://docs.astral.sh/uv/) and Python 3.13.

```bash
uv sync
uv run ai-tax-desk-api
```

With Docker:

```bash
docker build -t ai-tax-desk-api .
docker run --rm ai-tax-desk-api
```

Configuration is read from environment variables; copy `.env.example` to `.env` and fill it in.
Never commit `.env`.