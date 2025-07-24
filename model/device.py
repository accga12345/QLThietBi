from pydantic import BaseModel
from typing import Optional

class Device(BaseModel):
    device_id : Optional[int] = None
    name: str
    category_id: int
    quantity: int
    price: float
    manufacturer: str
    description: str
    status: str
