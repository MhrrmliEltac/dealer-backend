import base64
import uuid
import os
from fastapi import APIRouter, status, HTTPException
from tortoise.exceptions import DoesNotExist

from about.models import About
from about.schemas import ValidateAbout
from utils.paths import static_url_to_path, upload_dir

router = APIRouter()

UPLOAD_DIR = upload_dir("about")


@router.get("/")
async def get_about():
    about = await  About.first()
    return {"about": about}


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_about(data: ValidateAbout):
    about_image_url = None
    mission_image_url = None

    if data.about_image:
        if "," in data.about_image:
            header, b64_data = data.about_image.split(",", 1)
        else:
            b64_data = data.about_image

        file_name = f"{uuid.uuid4()}.webp"
        file_path = os.path.join(UPLOAD_DIR, file_name)

        with open(file_path, "wb") as f:
            f.write(base64.b64decode(b64_data))

        about_image_url = f"/static/uploads/about/{file_name}"

    if data.mission_image:
        if "," in data.mission_image:
            header, b64_data = data.mission_image.split(",", 1)
        else:
            b64_data = data.mission_image

        file_name = f"{uuid.uuid4()}.webp"
        file_path = os.path.join(UPLOAD_DIR, file_name)

        with open(file_path, "wb") as f:
            f.write(base64.b64decode(b64_data))

        mission_image_url = f"/static/uploads/about/{file_name}"

    new_about = await About.create(
        about=data.about,
        about_desc=data.about_desc,
        about_image=about_image_url,
        mission=data.mission,
        mission_desc=data.mission_desc,
        mission_image=mission_image_url,
    )

    return {
        "detail": "About created successfully",
        "about": new_about,
    }


@router.delete("/{about_id}")
async def delete_about(about_id: uuid.UUID):
    try:
        about = await About.get(id=about_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="About not found")

    if about.about_image:
        file_path = static_url_to_path(about.about_image)
        if os.path.exists(file_path):
            os.remove(file_path)

    elif about.mission_image:
        file_path = static_url_to_path(about.mission_image)
        if os.path.exists(file_path):
            os.remove(file_path)

    await about.delete()

    return {
        "detail": "About deleted successfully",
    }
