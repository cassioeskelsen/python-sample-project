import inject

from src.xpto.invoices.config.invoices_settings import InvoicesSettings
from src.xpto.invoices.repositories.invoice_repository import InvoiceRepository
from src.xpto.invoices.repositories.mongodb.MongoDBInvoiceRepository import MongoDBInvoiceRepository


def ioc_config(binder):
    invoice_settings = InvoicesSettings()
    binder.bind(InvoicesSettings, invoice_settings)
    binder.bind(InvoiceRepository, MongoDBInvoiceRepository(invoice_settings))


def register_ioc():
    inject.configure(ioc_config)
