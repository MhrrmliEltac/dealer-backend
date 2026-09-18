import base64
import uuid
import os
from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist
from services.models import Services
from services.schemas import ValidateService
from utils.paths import static_url_to_path, upload_dir

router = APIRouter()

UPLOAD_DIR = upload_dir("services")


@router.get("/")
async def get_services():
    services = await Services.all()
    return services


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_service(data: ValidateService):
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

        image_url = f"/static/uploads/services/{file_name}"

    new_service = await Services.create(
        title=data.title,
        image=image_url,
        description=data.description
    )
    return {
        "detail": "Service created successfully",
        "service": new_service
    }


@router.delete("/{service_id}")
async def delete_service(service_id: uuid.UUID):
    try:
        service = await Services.get(id=service_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )

    if service.image:
        file_path = static_url_to_path(service.image)
        if os.path.exists(file_path):
            os.remove(file_path)

    await service.delete()

    return {
        "detail": "Service deleted successfully"
    }
