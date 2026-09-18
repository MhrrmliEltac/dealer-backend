from pydantic import BaseModel
from typing import Optional


class RequestAdvantages(BaseModel):
    title: str
    description: Optional[str] = None
    image: Optional[str] = None
