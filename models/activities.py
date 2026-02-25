from sqlalchemy import Column, Integer, String, Boolean,Text
from db.database import Base



class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    activity_name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    activity_percentage=Column(Integer,nullable=True)

    