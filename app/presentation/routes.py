from fastapi import APIRouter
from app.interface.order_controller import OrderController
from app.domain.schemas import OrderCreate, OrderResponse

router = APIRouter()
order_controller = OrderController()

@router.post("/orders/", response_model=OrderResponse)
def create_order(order_data: OrderCreate):
    return order_controller.create_order(order_data)

@router.get("/orders/")
def get_orders():
    return order_controller.get_orders()

@router.get("/orders/{order_id}")
def get_order_by_id(order_id: int):
    return order_controller.get_order_by_id(order_id)
