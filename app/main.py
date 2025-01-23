from fastapi import FastAPI
from app.controller.payment_controller import router as payment_router
from app.model.payment_model import meta
from app.config.db import engine

# Initialize the database
meta.create_all(engine)

# Initialize FastAPI
app = FastAPI()

# Add routes
app.include_router(payment_router, prefix="/api/v1")