from pydantic import BaseModel
class SelfAssessmentCreate(BaseModel):
    q1: float
    q2: float
    q3: float
    q4: float
    q5: float
    q6: float
class SelfAssessmentResponse(BaseModel):
    user_id: int
    total_score: float
    percentage: float
    risk_level: str
    model_config = {"from_attributes": True}

























# from pydantic import BaseModel
# from datetime import datetime

# class SelfAssessmentCreate(BaseModel):
#     user_id: int
#     score: int
#     addiction_level: str
#     test_date: datetime

# class SelfAssessmentResponse(SelfAssessmentCreate):
#     test_id: int

#     class Config:
#         orm_mode = True
