from fastapi import APIRouter, HTTPException, status
from user.models import User
from user.schemas import ValidateSignUp, ValidateSignIn, ResponseUser
from tortoise.expressions import Q

from utils.hashing import Hash
from utils.token_manager import TokenManager

router = APIRouter()


@router.post("/sign-up", response_model=ResponseUser, status_code=status.HTTP_201_CREATED)
async def sign_up(data: ValidateSignUp):
    user = await User.get_or_none(Q(email=data.email))

    if user:
        raise HTTPException(status_code=400, detail="Email already exists")
    else:
        user = await User(
            email=data.email,
            fullname=data.fullname,
            phone_number=data.phone_number,
            monthly_volume=data.monthly_volume,
            suggestion=data.suggestion,
        )
        user.set_password(data.password)
        await user.save()
        return {
            "detail": "Sign up successful",
            "user": user,
        }


@router.post("/sign-in", response_model=ResponseUser)
async def sign_in(data: ValidateSignIn):
    if not data.email:
        raise HTTPException(status_code=400, detail="Email not provided")

    user = await User.get_or_none(email=data.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not found ")
    verify = Hash.decrypt(data.password, user.password)
    if verify:
        access_token = TokenManager.create_token({"id": user.id})
        return {"detail": "Sign in successful", "user": user, "access_token": access_token}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
