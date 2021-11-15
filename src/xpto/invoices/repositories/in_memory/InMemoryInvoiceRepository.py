from src.xpto.invoices.models.invoice import Invoice
from src.xpto.invoices.repositories.invoice_repository import InvoiceRepository


class InMemoryInvoiceRepository(InvoiceRepository):

    def add(self, invoice: Invoice):
        print(f"add from {self.__class__.__name__}")

    def get(self) -> list[Invoice]:
        print(f"get from {self.__class__.__name__}")
