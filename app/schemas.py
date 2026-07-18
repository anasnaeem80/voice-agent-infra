from pydantic import BaseModel


class CallRequest(BaseModel):

    patient_name: str

    date_of_birth: str | None = None

    phone_number: str | None = None

    reason: str | None = None