from fastapi import FastAPI

from database import engine
from models import Base

from routes.health import router as health_router
from routes.webhook import router as webhook_router
from routes.metrics import router as metrics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Voice Agent Backend",
    description="Backend service for the Vapi Healthcare Voice Agent",
    version="1.0.0"
)

app.include_router(health_router, tags=["Health"])
app.include_router(webhook_router, tags=["Webhook"])
app.include_router(metrics_router, tags=["Metrics"])


@app.get("/", tags=["Root"])
def root():
    return {
        "application": "Voice Agent Backend",
        "status": "running",
        "version": "1.0.0"
    }