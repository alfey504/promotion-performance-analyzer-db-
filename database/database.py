from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

db_conn = os.getenv("DB_CONN")
if db_conn is None:
    print("DB_CONN not found in .env")

sql_engine = create_engine(db_conn)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(
    bind=sql_engine,
    autoflush = False,
    autocommit=False,
)
