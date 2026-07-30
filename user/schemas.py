from enum import Enum

from fastapi import HTTPException, status
from pydantic import BaseModel, field_validator

from utils.check_email import CheckEmail
from utils.check_password import CheckPassword
from utils.check_fullname import CheckFullname

class ValidateSignUp(BaseModel):
    fullname: str
    phone_number: str
    email: str
    password: str
    monthly_volume: int
    suggestion: str

    @field_validator("email")
    def email_validator(cls, email: str):
        if not CheckEmail.check_email(email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email address. Please enter a valid email format (e.g., user@example.com)."
            )
        return email

    @field_validator("password")
    def password_validator(cls, password: str):
        if not CheckPassword.check_password(password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid password. Password must be at least 8 characters and include an uppercase letter, a lowercase letter, and a number."
            )
        return password

    @field_validator("fullname")
    def fullname_validator(cls, fullname: str):
        if not CheckFullname.check_fullname(fullname):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid full name. Full name must contain only letters and cannot include numbers or special characters."
            )
        return fullname


class ValidateSignIn(BaseModel):
    email: str
    password: str

    @field_validator("email")
    def email_validator(cls, email: str):
        if not CheckEmail.check_email(email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Email")
        return email

    @field_validator("password")
    def password_validator(cls, password: str):
        if not CheckPassword.check_password(password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")
        return password


class UserOut(BaseModel):
    email: str
    fullname: str
    phone_number: str
    monthly_volume: int
    suggestion: str

    class Config:
        from_attributes = True


class ResponseUser(BaseModel):
    detail: str
    user: UserOut
    access_token: str | None = None