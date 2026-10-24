import os


def main() -> None:
    import uvicorn

    from ai_tax_desk_api.entrypoints.http import app

    # In a container, 127.0.0.1 is the container's own loopback; the Dockerfile sets HOST=0.0.0.0.
    uvicorn.run(
        app, host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", "8002"))
    )
