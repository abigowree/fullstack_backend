from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from db.database import get_db
from models.user_activity import UserActivity
from schemas.user_activity import UserActivityCreate, UserActivityResponse

router = APIRouter(
    prefix="/user-activities",
    tags=["User Activities"]
)




@router.post("/", response_model=UserActivityResponse)
def start_activity(
    data: UserActivityCreate,
    db: Session = Depends(get_db)
):
    new_activity = UserActivity(
        user_id=data.user_id,
        activity_id=data.activity_id,
        status=data.status
    )

    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity


@router.get("/user/{user_id}", response_model=list[UserActivityResponse])
def get_user_activities(
    user_id: int,
    db: Session = Depends(get_db)
):
    return db.query(UserActivity)\
             .filter(UserActivity.user_id == user_id)\
             .all()


@router.put("/{user_activity_id}/complete")
def complete_activity(
    user_activity_id: int,
    db: Session = Depends(get_db)
):
    activity = db.query(UserActivity)\
                 .filter(UserActivity.id == user_activity_id)\
                 .first()

    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    activity.status = "completed"
    activity.completed_at = func.now()

    db.commit()
    db.refresh(activity)

    return {
        "message": "Activity marked as completed",
        "activity_id": activity.id,
        "status": activity.status,
        "completed_at": activity.completed_at
    }

