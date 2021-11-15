from src.xpto.common.models.order import Order
from src.xpto.orders.repositories.order_repository import OrderRepository


class InMemoryOrderRepository(OrderRepository):

    def add(self, invoice: Order):
        print(f"add from {self.__class__.__name__}")

    def get(self) -> list[Order]:
        print(f"get from {self.__class__.__name__}")
