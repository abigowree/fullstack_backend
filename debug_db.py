
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.users import User
from core.auth_utils import get_password_hash, verify_password

def fix_passwords():
    print("Connecting to database...")
    db = SessionLocal()
    try:
        users = db.query(User).all()
        print(f"Found {len(users)} users. Checking passwords...")
        
        fixed_count = 0
        for user in users:
            try:
                # Attempt to verify a dummy password. 
                # If the hash format is bad, this will raise UnknownHashError
                verify_password("test", user.password)
            except Exception as e:
                print(f"User {user.email} has INVALID hash. Resetting to 'password123'")
                user.password = get_password_hash("password123")
                fixed_count += 1
        
        if fixed_count > 0:
            db.commit()
            print(f"Successfully fixed {fixed_count} users.")
        else:
            print("All users have valid password hashes.")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    fix_passwords()
