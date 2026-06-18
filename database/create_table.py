from database.database import sql_engine, Base

from database.models import (
    Product,
    Customer,
    Promotion,
    Fulfillments,
    Sale,
)

def init_tables():
    Base.metadata.create_all(bind=sql_engine)