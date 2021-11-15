from abc import abstractmethod
from typing import Protocol, runtime_checkable

from src.xpto.common.models.order import Order


@runtime_checkable
class OrderRepository(Protocol):

    @abstractmethod
    def add(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def get(self) -> list[Order]:
        pass
