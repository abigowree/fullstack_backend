from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from models.activities import Activity
from schemas.activities import ActivityCreate, ActivityResponse

router = APIRouter(
    prefix="/activities",
    tags=["Activities"]
)

@router.post("/", response_model=ActivityResponse)
def create_activity(data: ActivityCreate, db: Session = Depends(get_db)):
    activity = Activity(
        activity_name=data.activity_name,
        activity_percentage=data.activity_percentage,
        description=data.description
    )
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity


@router.get("/", response_model=list[ActivityResponse])
def get_all_activities(db: Session = Depends(get_db)):
    return db.query(Activity).all()




@router.get("/get/activities/{percentage}")
def get_activities(percentage:int, db:Session = Depends(get_db)):
    activities = db.query(Activity).filter(percentage >= Activity.activity_percentage).all()
    return activities 