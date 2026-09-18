from fastapi import APIRouter, status, HTTPException
from cars.schemas import RequestCar
from cars.models import Cars

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_car(data: RequestCar):

    car = await Cars.get_or_none(vincode=data.vincode)

    if car:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="VIN code must be unique"
        )

    new_car = await Cars.create(
        name=data.name, description=data.description, vincode=data.vincode
    )

    return {"message": "Cars created successfully", "detail": new_car}


@router.get("/")
async def get_car_by_vin(vincode: str):
    car = await Cars.get(vincode=vincode)

    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Car not found"
        )

    return {"data": car}
