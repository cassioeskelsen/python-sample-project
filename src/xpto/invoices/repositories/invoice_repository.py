from abc import abstractmethod
from typing import Protocol, runtime_checkable

from src.xpto.invoices.models.invoice import Invoice


@runtime_checkable
class InvoiceRepository(Protocol):

    @abstractmethod
    def add(self, invoice: Invoice):
        pass

    @abstractmethod
    def get(self) -> list[Invoice]:
        pass
