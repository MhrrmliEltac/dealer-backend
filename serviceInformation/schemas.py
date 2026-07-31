from typing import List

from pydantic import BaseModel


class ValidateServiceInfo(BaseModel):
    title: str
    description: str
    tags: List[str]
    image_url: str
