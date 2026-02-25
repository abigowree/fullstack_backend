
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import DB_HOSTNAME, DB_PASSWORD, DB_PORT, DB_USERNAME, DATABASE

DB_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DATABASE}"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

Base = declarative_base()

# ✅ ADD THIS (IMPORTANT)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from dotenv import load_dotenv
# import os


# load_dotenv()


# DB_USERNAME = os.getenv("DB_USERNAME")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOSTNAME = os.getenv("DB_HOSTNAME")
# DB_PORT = os.getenv("DB_PORT")
# DATABASE = os.getenv("DATABASE")


# DATABASE_URL = (
#     f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}"
#     f"@{DB_HOSTNAME}:{DB_PORT}/{DATABASE}"
# )


# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()


