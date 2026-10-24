from fastapi import FastAPI

app = FastAPI(title="ai-tax-desk-api")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
