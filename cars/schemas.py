from pydantic import BaseModel, field_validator


class RequestCar(BaseModel):
    name: str
    description: str
    vincode: str

    @field_validator("vincode")
    @classmethod
    def check_vin_code(cls, value):
        if not value or not value.strip():
            raise ValueError("Vin code is required")
        if len(value) != 17:
            raise ValueError("VIN code must be exactly 17 characters")
        if any(char in value for char in "IOQ"):
            raise ValueError("VIN code must not contain I, O or Q characters")

        upper_value = value.upper()

        if not upper_value.isupper():
            raise ValueError("VIN code must contain only uppercase characters")

        return upper_value

    @field_validator("name")
    @classmethod
    def check_name(cls, value):
        if not value or not value.strip():
            raise ValueError("Car name is required")
        return value

    @field_validator("description")
    @classmethod
    def check_description(cls, value):
        if not value or not value.strip():
            raise ValueError("Car description is required")
        return value
