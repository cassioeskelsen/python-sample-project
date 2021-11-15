import inject

from src.xpto.common.models.order import Order
from src.xpto.orders.config.orders_settings import OrdersSettings
from src.xpto.orders.repositories.order_repository import OrderRepository


class MongoDBOrderRepository(OrderRepository):

    def __init__(self, settings: OrdersSettings):
        print(f"Connecting to {settings.mongodb_conn_string}")

    def get_order_by_id(self, order_id: int) -> Order:
        order = Order(customer_name='xyz')
        order.id = order_id
        return order

    def add(self, order: Order) -> Order:
        print(f"add from {self.__class__.__name__}")
        return order

    def get(self) -> list[Order]:
        print(f"get from {self.__class__.__name__}")
