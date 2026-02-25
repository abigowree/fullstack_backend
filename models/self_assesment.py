from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
 
from db.database import Base
class SelfAssessment(Base):
    __tablename__ = "self_assessment"   
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    q1 = Column(Float, nullable=False)
    q2 = Column(Float, nullable=False)
    q3 = Column(Float, nullable=False)
    q4 = Column(Float, nullable=False)
    q5 = Column(Float, nullable=False)
    q6 = Column(Float, nullable=False)
    total_score = Column(Float, nullable=False)
    percentage = Column(Float, nullable=False)
    risk_level = Column(String, nullable=False)
   

