import base64
import os
import uuid

from fastapi import APIRouter
from starlette import status

from serviceInformation.models import ServiceInfo
from serviceInformation.schemas import ValidateServiceInfo
from utils.paths import upload_dir

router = APIRouter()

UPLOAD_DIR = upload_dir("serviceInfo")


@router.get("/")
async def get_service_info():
    all_service_info = await ServiceInfo.all()
    return all_service_info


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_service_info(data: ValidateServiceInfo):
    image_url = None

    if data.image_url:
        if "," in data.image_url:
            header, b64_data = data.image_url.split(",")
        else:
            b64_data = data.image_url

        file_name = f"{uuid.uuid4()}.webp"
        file_path = os.path.join(UPLOAD_DIR, file_name)

        with open(file_path, "wb") as f:
            f.write(base64.b64decode(b64_data))
        image_url = f"/static/uploads/serviceInfo/{file_name}"

    new_service_info = await ServiceInfo.create(title=data.title, description=data.description, tags=data.tags,
                                                image=image_url)
    return {
        "id": new_service_info.id,
        "detail": "Service info created successfully",
        "new_service_info": new_service_info
    }


@router.delete("/")
async def delete_all_service_info():
    deleted_count = await ServiceInfo.all().delete()
    return {
        "detail": "All service info deleted successfully",
        "deleted_count": deleted_count
    }
