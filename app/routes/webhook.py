from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.post("/webhook")
async def webhook(payload: dict):

    print("=" * 60)
    print("Webhook received")
    print(datetime.utcnow())
    print(payload)
    print("=" * 60)

    return {
        "success": True,
        "message": "Webhook received"
    }
