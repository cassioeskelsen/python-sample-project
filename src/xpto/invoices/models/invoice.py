import dataclasses
import random
from pydantic.dataclasses import dataclass

from src.xpto.common.models.order import Order


@dataclass
class Invoice:
    id: int = dataclasses.field(init=False)
    order: Order

    def __post_init__(self):
        self.id = random.randint(1, 100_000)
