from app.infra.repositories import OrderRepository
from app.domain.schemas import OrderCreate, OrderResponse

class OrderUseCase:
    """Caso de uso para criação e consulta de pedidos."""

    def __init__(self):
        self.order_repository = OrderRepository()

    def create_order(self, order_data: OrderCreate) -> OrderResponse:
        """Executa a criação do pedido."""
        if order_data.total_price <= 0:
            raise ValueError("O preço total deve ser maior que zero.")

        new_order = self.order_repository.create_order(order_data)

        return OrderResponse(
            id=new_order.id,
            customer_name=new_order.customer_name,
            total_price=new_order.total_price,
            status=new_order.status
        )

    def get_orders(self):
        """Busca todos os pedidos."""
        return self.order_repository.get_orders()

    def get_order_by_id(self, order_id: int):
        """Busca um pedido pelo ID."""
        return self.order_repository.get_order_by_id(order_id)
