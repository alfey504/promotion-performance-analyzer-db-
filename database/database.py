from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

db_conn = ""

sql_engine = create_engine(db_conn)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(
    bind=sql_engine,
    autoflush = False,
    autocommit=False,
)
