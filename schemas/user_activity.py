from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserActivityUpdate(BaseModel):
    status: str 

class UserActivityCreate(BaseModel):
    user_id: int
    activity_id: int
    status: str = "started"

class UserActivityResponse(BaseModel):
    id: int
    user_id: int
    activity_id: int
    status: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    

    


    class Config:
        from_attributes = True
