from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas import CallRequest
from crud import create_call

router = APIRouter()


@router.post("/webhook")
async def webhook(
    payload: CallRequest,
    db: Session = Depends(get_db)
):
    try:
        call = create_call(db, payload)

        return {
            "success": True,
            "message": "Call stored successfully",
            "id": call.id
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to store call: {str(e)}"
        )