from pydantic import BaseModel
from typing import Optional

class ValidateService(BaseModel):
    title: str
    description: Optional[str] = None
    image: Optional[str] = None



