from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class CallRecord(Base):
    __tablename__ = "call_records"

    id = Column(Integer, primary_key=True, index=True)

    patient_name = Column(String(255), nullable=False)

    date_of_birth = Column(String(50), nullable=True)

    phone_number = Column(String(50), nullable=True)

    reason = Column(String(500), nullable=True)

    status = Column(String(100), default="received")

    created_at = Column(DateTime, default=datetime.utcnow)