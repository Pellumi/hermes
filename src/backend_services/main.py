from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, missions

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hermes Backend API",
    description="API for Hermes Drone Delivery System",
    version="0.1.0"
)

app.include_router(auth.router)
app.include_router(missions.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Hermes Backend API"}
