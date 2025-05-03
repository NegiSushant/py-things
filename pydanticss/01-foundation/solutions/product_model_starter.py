# TODO: Create product model with id, name, price, in_stock

from pydantic import BaseModel #type: ignore

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stocks: bool = True