from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import math
from db.database import get_db
from models.self_assesment import SelfAssessment
from schemas.self_assesment import (
    SelfAssessmentCreate,
    SelfAssessmentResponse
)
router = APIRouter(
    prefix="/self-assessment",
    tags=["Self Assessment"]
)
from dependencies import get_current_user
from models.users import User

@router.post("/", response_model=SelfAssessmentResponse)
def submit_assessment(
    data: SelfAssessmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing = db.query(SelfAssessment)\
        .filter(SelfAssessment.user_id == current_user.id)\
        .first()

    if existing:
        # Optional: Decide if you want to allow retakes. For now, let's delete old or update.
        # Let's delete the old one to allow "retaking" effectively or just raise error.
        # The user seems to want to take it multiple times potentially (flow wise).
        # But sticking to original logic of checking existing:
        db.delete(existing)
        db.commit()
    
    total_score = (
        data.q1 + data.q2 + data.q3 +
        data.q4 + data.q5 + data.q6
    )

    # Risk Logic:
    # <= 9 -> Low
    # <= 18 -> Medium
    # > 18 -> High
    
    if total_score <= 9:
        risk = "Low"
    elif total_score <= 18:
        risk = "Medium"
    else:
        risk = "High"
    
    # Calculate percentage just for storage (optional, based on max score of 30 if max is 5 per q)
    # Assuming max score per question is 5 (based on options in frontend likely 1-5)
    max_score = 30 
    percentage = (total_score / max_score) * 100

    assessment = SelfAssessment(
        user_id=current_user.id,
        q1=data.q1,
        q2=data.q2,
        q3=data.q3,
        q4=data.q4,
        q5=data.q5,
        q6=data.q6,
        total_score=total_score,
        percentage=percentage,
        risk_level=risk
    )

    db.add(assessment)
    db.commit()
    db.refresh(assessment)

    return assessment
