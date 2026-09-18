import base64
import uuid
import os
from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist
from advantages.models import Advantages
from advantages.schemas import RequestAdvantages
from utils.paths import static_url_to_path, upload_dir

router = APIRouter()

UPLOAD_DIR = upload_dir("advantages")


@router.get("/")
async def get_advantages():
    advantages = await Advantages.all()
    return advantages


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_advantage(data: RequestAdvantages):
    image_url = None
    if data.image:
        if "," in data.image:
            header, b64_data = data.image.split(",", 1)
        else:
            b64_data = data.image

        file_name = f"{uuid.uuid4()}.webp"
        file_path = os.path.join(UPLOAD_DIR, file_name)

        with open(file_path, "wb") as f:
            f.write(base64.b64decode(b64_data))

        image_url = f"/static/uploads/advantages/{file_name}"

    new_advantage = await Advantages.create(
        title=data.title, image=image_url, description=data.description
    )

    return {"detail": "Advantage created successfully", "advantage": new_advantage}


@router.delete("/{advantage_id}")
async def delete_advantage(advantage_id: uuid.UUID):
    try:
        advantage = await Advantages.get(id=advantage_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Advantage not found"
        )

    if advantage.image:
        file_path = static_url_to_path(advantage.image)
        if os.path.exists(file_path):
            os.remove(file_path)

    await advantage.delete()

    return {"detail": "Advantage deleted successfully"}
