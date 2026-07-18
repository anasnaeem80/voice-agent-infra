from sqlalchemy.orm import Session
from models import CallRecord
from schemas import CallRequest


def create_call(db: Session, payload: CallRequest):

    call = CallRecord(
        patient_name=payload.patient_name,
        date_of_birth=payload.date_of_birth,
        phone_number=payload.phone_number,
        reason=payload.reason,
        status="received"
    )

    db.add(call)
    db.commit()
    db.refresh(call)

    return call