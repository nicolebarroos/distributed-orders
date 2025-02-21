from app.application.use_cases.order_use_case import OrderUseCase
from app.domain.schemas import OrderCreate, OrderResponse

class OrderController:
    def __init__(self):
        self.use_case = OrderUseCase()

    def create_order(self, order_data: OrderCreate) -> OrderResponse:
        """Chama o caso de uso para criar um pedido."""
        return self.use_case.create_order(order_data)

    def get_orders(self):
        """Chama o caso de uso para buscar todos os pedidos."""
        return self.use_case.get_orders()

    def get_order_by_id(self, order_id: int):
        """Chama o caso de uso para buscar um pedido pelo ID."""
        return self.use_case.get_order_by_id(order_id)
