from pydantic import BaseModel


class ValidateAuction(BaseModel):
    title: str
    image: str
