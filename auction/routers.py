from fastapi import APIRouter, HTTPException, status
from auction.models import Auction
from auction.schemas import ValidateAuction

router = APIRouter()


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
    if not auction.title or not auction.image:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Auction can not be created")

    new_auction = await Auction.create(title=auction.title, image=auction.image)
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
