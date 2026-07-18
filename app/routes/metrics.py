from fastapi import APIRouter
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

router = APIRouter()

REQUEST_COUNTER = Counter(
    "voice_agent_requests_total",
    "Total API Requests"
)

@router.get("/metrics")
def metrics():

    REQUEST_COUNTER.inc()

    return Response(
        generate_latest(),
        media_type="text/plain"
    )
