from pydantic import BaseModel, Field

class OrderCreate(BaseModel):
    customer_name: str = Field(..., title="Customer Name", min_length=3, max_length=100)
    total_price: float = Field(..., title="Total Price", gt=0)

class OrderResponse(OrderCreate):
    id: int
    status: str
