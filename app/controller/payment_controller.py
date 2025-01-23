from fastapi import APIRouter, HTTPException
from app.schema.payment_schema import PaymentSchema
from app.service.payment_service import PaymentService

router = APIRouter()

@router.get("/payments")
def get_all_payments():
    return PaymentService.fetch_all_payments()

@router.get("/payments/{payment_id}")
def get_payment_by_id(payment_id: int):
    payment = PaymentService.fetch_payment_by_id(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.post("/payments")
def create_payment(payment: PaymentSchema):
    print(payment.dict())
    return PaymentService.add_payment(payment.dict())

@router.put("/payments/{payment_id}")
def update_payment(payment_id: int, payment: PaymentSchema):
    return PaymentService.modify_payment(payment_id, payment.dict())

@router.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):
    return PaymentService.remove_payment(payment_id)