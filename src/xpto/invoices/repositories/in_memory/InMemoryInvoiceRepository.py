from src.xpto.common.utils.logger import logger
from src.xpto.invoices.models.invoice import Invoice
from src.xpto.invoices.repositories.invoice_repository import InvoiceRepository


class InMemoryInvoiceRepository(InvoiceRepository):

    def add(self, invoice: Invoice):
        logger.info(f"add from {self.__class__.__name__}")

    def get(self) -> list[Invoice]:
        logger.info(f"get from {self.__class__.__name__}")
