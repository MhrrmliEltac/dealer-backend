from fastapi import HTTPException
from pydantic import BaseModel, field_validator
from utils.check_email import CheckEmail


class ValidateContact(BaseModel):
    location: str
    email: str
    phone: str

    @field_validator("email")
    def validate_email(cls, email):
        if not CheckEmail.check_email(email):
            raise HTTPException(status_code=400, detail="Invalid Email")
        return email
