import inject

from src.xpto.common.models.order import Order
from src.xpto.invoices.models.invoice import Invoice
from src.xpto.invoices.repositories.invoice_repository import InvoiceRepository


class CreateInvoiceService:

    @inject.autoparams()
    def create_from_order(self, order: Order, invoice_repository: InvoiceRepository) -> Invoice:
        inv = Invoice(order=order)
        invoice_repository.add(inv)
        return inv
