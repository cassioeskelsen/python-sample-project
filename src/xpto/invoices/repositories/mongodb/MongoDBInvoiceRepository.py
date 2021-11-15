from src.xpto.invoices.config.invoices_settings import InvoicesSettings
from src.xpto.invoices.models.invoice import Invoice
from src.xpto.invoices.repositories.invoice_repository import InvoiceRepository


class MongoDBInvoiceRepository(InvoiceRepository):

    def __init__(self, invoice_settings: InvoicesSettings):
        print(f"Connecting to {invoice_settings.mongodb_conn_string}")

    def add(self, invoice: Invoice):
        print(f"add from {self.__class__.__name__}")

    def get(self) -> list[Invoice]:
        print(f"get from {self.__class__.__name__}")
