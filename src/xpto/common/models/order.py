import dataclasses
import random
from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class Order:
    """
    Esse model é apenas para fins de exemplo,
    obviamente os campos de um sistema real não seriam esses
    """
    id: int = dataclasses.field(init=False)
    order_date: datetime = dataclasses.field(default=None, init=False)
    customer_name: str

    def __post_init__(self):
        self.id = random.randint(1, 100_000)
        self.order_date = datetime.now()
