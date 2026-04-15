from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.activities import Activity

def inspect_activities():
    db = SessionLocal()
    try:
        activities = db.query(Activity).all()
        print(f"Total activities: {len(activities)}")
        for a in activities:
            print(f"ID: {a.id}, Name: {a.activity_name}, Percentage: {a.activity_percentage}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    inspect_activities()
