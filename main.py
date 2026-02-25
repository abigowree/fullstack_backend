from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user_activity, activities, self_assesment, users
from db.database import Base, engine

app = FastAPI(title="Screen Free API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; refine for production
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(activities.router)
app.include_router(self_assesment.router)
app.include_router(users.router)
app.include_router(user_activity.router)


