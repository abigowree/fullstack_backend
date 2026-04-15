from pydantic import BaseModel


class ActivityCreate(BaseModel):
    activity_name: str
    description: str | None = None
    activity_percentage:int

class ActivityResponse(BaseModel):
    id: int
    activity_name: str
    description: str | None
    activity_percentage: int | None

    class Config:
        from_attributes = True
