from pydantic import BaseModel

class PaymentSchema(BaseModel):
    upi_id: str
    amount: int
    status: str