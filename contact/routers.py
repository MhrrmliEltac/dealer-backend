from fastapi import APIRouter, HTTPException, status
from contact.models import Contact
from contact.schemas import ValidateContact

router = APIRouter()


@router.get("/")
async def get_contact():
    contact = await Contact.all()
    return contact


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_contact(data: ValidateContact):
    if not data.email or not data.location or not data.phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or location not provided",
        )

    new_contact = await Contact.create(location=data.location, email=data.email, phone=data.phone)
    return {
        "detail": "Contact created successfully",
        "contact": new_contact,
    }
