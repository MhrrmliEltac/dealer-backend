from pydantic import BaseModel


class ValidateAbout(BaseModel):
    about: str
    about_desc: str
    about_image: str
    mission: str
    mission_desc: str
    mission_image: str
