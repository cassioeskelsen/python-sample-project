import inject
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from src.xpto.common.models.order import Order
from src.xpto.orders.ioc_orders import register_ioc
from src.xpto.orders.repositories.order_repository import OrderRepository

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


@app.get("/get_order")
def get_order(order_id: int):
    order = inject.instance(OrderRepository).get_order_by_id(order_id)
    return {"invoice": jsonable_encoder(order)}


@app.post("/create_order")
def create_order(order: Order):
    order = inject.instance(OrderRepository).add(order)
    return {"invoice": jsonable_encoder(order)}
