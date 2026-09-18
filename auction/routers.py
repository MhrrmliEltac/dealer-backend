import base64
import uuid
import os
from fastapi import APIRouter, HTTPException, status
from auction.models import Auction
from auction.schemas import ValidateAuction
from utils.paths import upload_dir

router = APIRouter()

UPLOAD_DIR = upload_dir("auction")


@router.get("/")
async def get_auction_about():
    all_auction = await Auction.all()
    return all_auction


@router.get("/{auction_id}")
async def get_auction(auction_id: int):
    auction = await Auction.filter(id=auction_id).first()

    if not auction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Auction not found")
    return auction


@router.post("/")
async def create_auction(auction: ValidateAuction):
    image_url = None
    if auction.image:
        if "," in auction.image:
            header, b64_data = auction.image.split(",", 1)
        else:
            b64_data = auction.image

        file_name = f"{uuid.uuid4()}.webp"
        file_path = os.path.join(UPLOAD_DIR, file_name)

        with open(file_path, "wb") as f:
            f.write(base64.b64decode(b64_data))

        image_url = f"/static/uploads/auction/{file_name}"
    new_auction = await Auction.create(title=auction.title, image=image_url)
    return {
        "detail": "Auction created successfully",
        "auction": new_auction
    }


@router.put("/{auction_id}")
async def update_auction(auction_id: int, data: ValidateAuction):
    auction = await Auction.filter(id=auction_id).first()

    if not auction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Auction not found")
    auction.title = data.title
    auction.image = data.image
    await auction.save()
    return {
        "detail": "Auction updated successfully",
        "auction": auction
    }


@router.delete("/{auction_id}")
async def delete_auction(auction_id: int):
    auction = await Auction.filter(id=auction_id).first()
    if not auction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Auction not found")
    await auction.delete()
    return {
        "detail": "Auction deleted successfully",
    }
