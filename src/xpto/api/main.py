import httpx as httpx
import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from src.xpto.api.config.api_settings import ApiSettings
from src.xpto.common.models.order import Order

app = FastAPI()
api_settings = ApiSettings()


@app.get("/")
async def home():
    return {"hello": "world"}


@app.post("/order")
async def new_order(order: Order):
    ret = httpx.post(f"{api_settings.orders_api}/create_order", json={"customer_name": order.customer_name})
    return {"order": jsonable_encoder(ret.json())}


@app.post("/create_invoice")
async def create_invoice(order_id: int):
    ret = httpx.post(f"{api_settings.invoices_api}/create_invoice", params={"order_id": order_id})
    return {"invoice": jsonable_encoder(ret.json())}


if __name__ == "__main__":
    uvicorn.run("src.xpto.api.main:app", host="127.0.0.1", port=api_settings.http_port, log_level="info")
