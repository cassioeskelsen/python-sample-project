import inject

from src.xpto.orders.config.orders_settings import OrdersSettings
from src.xpto.orders.repositories.mongodb.MongoDBOrderRepository import MongoDBOrderRepository
from src.xpto.orders.repositories.order_repository import OrderRepository


def ioc_config(binder):
    orders_settings = OrdersSettings()
    binder.bind(OrdersSettings, orders_settings)
    binder.bind(OrderRepository, MongoDBOrderRepository(orders_settings))



def register_ioc():
    inject.configure(ioc_config)
