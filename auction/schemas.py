from pydantic import BaseModel
from typing import Optional


class ValidateAuction(BaseModel):
    title: str
    image: Optional[str] = None
