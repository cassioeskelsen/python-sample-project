from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from src.xpto.api.config.api_settings import CommonSettings, ApiSettings
from src.xpto.common.models.order import Order

app = FastAPI()


@app.get("/")
def home():
    return {"hello": "world"}


@app.post("/order")
def new_order(order: Order):
    return {"order": jsonable_encoder(order)}


@app.post("/create_invoice")
def create_invoice(order_id: int):
    pass
