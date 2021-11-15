import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from src.xpto.common.models.order import Order
from src.xpto.invoices.config.invoices_settings import InvoicesSettings
from src.xpto.invoices.ioc_invoices import register_ioc
from src.xpto.invoices.services.create_invoice_service import CreateInvoiceService

"""
    Esse é um exemplo de microsserviço que é chamado via API HTTP. Usei essa forma para simplificar o exemplo,
    mas em um sistema da vida real sugiro usar essa forma de comunicação entre microsserviços apenas em últimos
    casos. O ideal é que, sempre que possível, utilizemos uma arquitetura baseada em eventos para diminuir o 
    acoplamento entre os microsserviços.
    Veja minha série de artigos "Uma Arquitetura simples e eficiente para para sistemas event-driven em Python":
    https://eskelsen.medium.com/uma-arquitetura-simples-e-eficiente-para-sistemas-event-driven-em-python-parte-i-5eb59336d858
"""

app = FastAPI()
register_ioc()

invoices_settings = InvoicesSettings()


@app.post("/create_invoice")
async def create_invoice(order_id: int):
    # busca order de alguma forma, aqui não importa, vamos inicializar um novo obj
    order = Order(customer_name="teste123")
    service = CreateInvoiceService()
    invoice = service.create_from_order(order)
    return {"invoice": jsonable_encoder(invoice)}


if __name__ == "__main__":
    uvicorn.run("src.xpto.api.main:app", host="127.0.0.1", port=invoices_settings.http_port, log_level="info")
