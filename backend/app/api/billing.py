from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()

PLAN_PRICES = {
    "pro": 399,
    "producer": 799,
}


class InvoiceRequest(BaseModel):
    plan: str


@router.post("/create-invoice")
async def create_invoice(
    body: InvoiceRequest,
    current_user: User = Depends(get_current_user),
):
    """Создаёт invoice через Telegram Bot API."""
    if body.plan not in PLAN_PRICES:
        raise HTTPException(status_code=400, detail="Неверный план")

    # TODO: реализовать создание invoice через aiogram в Спринте 4
    return {"message": "Оплата будет реализована в Спринте 4", "plan": body.plan, "stars": PLAN_PRICES[body.plan]}


@router.post("/webhook")
async def billing_webhook(payload: dict):
    """Webhook от Telegram после успешной оплаты."""
    # TODO: реализовать обработку webhook в Спринте 4
    return {"ok": True}
