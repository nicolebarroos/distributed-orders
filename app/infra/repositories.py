from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.order import Order
from app.domain.schemas import OrderCreate
from app.infra.database import db_instance

class OrderRepository:
    def __init__(self):
        self.db: Session = db_instance.get_session()

    def create_order(self, order_data: OrderCreate) -> Order:
        """Cria um novo pedido no banco de dados."""
        new_order = Order(
            customer_name=order_data.customer_name,
            total_price=order_data.total_price,
            status="pending"
        )
        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        return new_order

    def get_orders(self) -> List[Order]:
        """Busca todos os pedidos."""
        return self.db.query(Order).all()

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        """Busca um pedido pelo ID."""
        return self.db.query(Order).filter(Order.id == order_id).first()
