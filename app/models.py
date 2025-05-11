from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


class User(BaseModel):
    id: int
    username: str
    email: str
