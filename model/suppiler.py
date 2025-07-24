from pydantic import BaseModel
from typing import Optional


class Supplier(BaseModel):
    supplier_id: Optional[int] = None
    name: str
    contact_person: str
    phone: str
    email: str
    address: str