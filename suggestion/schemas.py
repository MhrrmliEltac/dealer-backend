from pydantic import BaseModel, field_validator


class ValidateSuggestion(BaseModel):
    fullname: str
    phone_number: str
    suggestion: str

    @field_validator("fullname")
    @classmethod
    def fullname_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Full name is required")
        return v

    @field_validator("phone_number")
    @classmethod
    def phone_number_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Phone number is required")
        new_phone_number = v.split("+994")[-1]
        if not new_phone_number.isdigit() or len(new_phone_number) != 9:
            raise ValueError(
                "Phone number must be 9 digits long and contain only numbers"
            )
        return new_phone_number

    @field_validator("suggestion")
    @classmethod
    def suggestion_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Suggestion is required")
        return v
