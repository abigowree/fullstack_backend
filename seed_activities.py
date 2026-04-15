from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.activities import Activity

def seed_activities():
    db = SessionLocal()
    try:
        # Clear existing activities if any (optional, but good for consistent seeding)
        # db.query(Activity).delete() 
        
        activities = [
            # Low Intensity / Easy (0-30%)
            {"name": "Short Walk", "percentage": 10, "desc": "A brief 15-minute walk to clear your mind."},
            {"name": "Drinking Water", "percentage": 5, "desc": "Stay hydrated and take a screen break."},
            {"name": "Deep Breathing", "percentage": 15, "desc": "Practice 5 minutes of mindful breathing."},
            {"name": "Evening Jogging", "percentage": 25, "desc": "Improve stamina and refresh your mind."},
            {"name": "Cooking Practice", "percentage": 20, "desc": "Cook a healthy meal and improve your culinary skills."},
            
            # Medium Intensity (31-60%)
            {"name": "Gardening", "percentage": 45, "desc": "Maintain plants regularly and observe their growth."},
            {"name": "Project Build", "percentage": 50, "desc": "Start building your project (coding, creating or assembling)."},
            {"name": "New Skill", "percentage": 40, "desc": "Practice the skill step by step."},
            {"name": "Nature Walk", "percentage": 35, "desc": "A longer walk in a natural setting."},
            {"name": "Reading", "percentage": 55, "desc": "Read a physical book for 30 minutes."},
            
            # High Intensity (61-100%)
            {"name": "Workout", "percentage": 85, "desc": "Boost strength and endurance with a high intensity workout."},
            {"name": "Creative Writing", "percentage": 75, "desc": "Write essays, stories, or poems to sharpen creativity."},
            {"name": "Volunteering", "percentage": 70, "desc": "Help others and build strong social responsibility."},
            {"name": "Detox", "percentage": 90, "desc": "This activity improves focus, mental peace, and real-world awareness."},
            {"name": "Deep Work", "percentage": 80, "desc": "Work continuously with full focus."},
            {"name": "Brain Exercise", "percentage": 95, "desc": "Challenge yourself with increasing difficulty."},
            {"name": "Mindfulness", "percentage": 65, "desc": "Intense mindfulness and meditation session."}
        ]
        
        for act in activities:
            # Check if it exists to avoid duplicates
            existing = db.query(Activity).filter(Activity.activity_name == act["name"]).first()
            if not existing:
                new_act = Activity(
                    activity_name=act["name"],
                    activity_percentage=act["percentage"],
                    description=act["desc"]
                )
                db.add(new_act)
        
        db.commit()
        print("✅ Database seeded with activities successfully.")
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_activities()
