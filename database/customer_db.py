from database.database import SessionLocal
from database.utils import Conditions
from database.models import Customer
from sqlalchemy import select

def get_customer_by_condition(conditions: list[Conditions]) -> list[Customer]:
    condition_list = []
    sessison = SessionLocal()

    try:
        for condition in conditions:
            con = condition.parse_condition(Customer)
            condition_list.append(con)
        sessison.scalars(select(Customer).where(*condition_list)).all()
    except Exception as e:
        raise e
    finally:
        sessison.close()




        
