from fastapi import FastAPI

from routes.health import router as health_router
from routes.webhook import router as webhook_router
from routes.metrics import router as metrics_router

app = FastAPI(
    title="Voice Agent Backend",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(webhook_router)
app.include_router(metrics_router)


@app.get("/")
def root():
    return {
        "application": "Voice Agent Backend",
        "status": "running"
    }
