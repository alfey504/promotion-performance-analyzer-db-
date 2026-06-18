from database.database import SessionLocal
from sqlalchemy import select
from database.models import Product
from sqlalchemy import Sequence
from database.utils import Conditions

def get_all_products() ->  list[Product]:
    session = SessionLocal()
    
    try: 
        products = session.scalars(select(Product)).all()
        return list[Product](products)
    except Exception:
        return Exception("There was issues fetching data from the database")
    finally:
        session.close()

def get_products_by_condition(conditions: list[Conditions]) -> list[Product]:
    
    condition_list = []

    session = SessionLocal()
    try: 
        for condition in conditions:  
            con = condition.parse_condition(Product)     
            condition_list.append(con)

        products = session.scalars(select(Product).where(*condition_list)).all()
        return products
    except Exception as e:
        raise e
    finally:
        session.close()
    
