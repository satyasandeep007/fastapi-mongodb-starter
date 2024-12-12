from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user, order
from app.database import connect_to_mongo, close_mongo_connection

app = FastAPI(title="FastAPI MongoDB Boilerplate")

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(order.router, prefix="/api/orders", tags=["orders"])

@app.on_event("startup")
async def startup_db_client():
    print("Connecting to MongoDB...")
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    print("Closing MongoDB connection...")
    await close_mongo_connection()

@app.get("/")
async def root():
    print("Root endpoint called")
    return {"message": "Welcome to FastAPI MongoDB Boilerplate"}
