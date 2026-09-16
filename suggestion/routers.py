from fastapi import APIRouter, HTTPException, status

from suggestion.models import Suggestion
from suggestion.schemas import ValidateSuggestion

router = APIRouter()


@router.get("/")
async def get_suggestions():
    suggestions = await Suggestion.all()
    return suggestions


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_suggestion(data: ValidateSuggestion):
    if not data.fullname or not data.phone_number or not data.suggestion:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Fullname, phone number or suggestion not provided",
        )

    new_suggestion = await Suggestion.create(
        fullname=data.fullname,
        phone_number=data.phone_number,
        suggestion=data.suggestion,
    )
    return {
        "detail": "Suggestion created successfully",
        "suggestion": new_suggestion,
    }
