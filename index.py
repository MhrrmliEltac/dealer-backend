import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from config import tortoise_config
from user.routers import router as auth_router
from auction.routers import router as auction_router
from services.routers import router as service_router
from contact.routers import router as contact_router
from about.routers import router as about_router
from serviceInformation.routers import router as service_info_router
from suggestion.routers import router as suggestion_router
from advantages.routers import router as advantage_router
from cars.routers import router as cars_router

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(auction_router, prefix="/auction", tags=["Auction"])
app.include_router(service_router, prefix="/service", tags=["Service"])
app.include_router(contact_router, prefix="/contact", tags=["Contact"])
app.include_router(about_router, prefix="/about", tags=["About"])
app.include_router(service_info_router, prefix="/info", tags=["Info"])
app.include_router(suggestion_router, prefix="/suggestion", tags=["Suggestion"])
app.include_router(advantage_router, prefix="/advantage", tags=["Advantage"])
app.include_router(cars_router, prefix="/cars", tags=["Cars"])

tortoise_config(
    app,
    [
        "user.models",
        "auction.models",
        "contact.models",
        "services.models",
        "about.models",
        "serviceInformation.models",
        "suggestion.models",
        "advantages.models",
        "cars.models",
    ],
)

if __name__ == "__main__":
    uvicorn.run(app="index:app", port=8080, reload=True, host="127.1.1.1")
