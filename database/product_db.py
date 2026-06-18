from database.database import SessionLocal
from sqlalchemy import select
from database.models import Product
from sqlalchemy import Sequence
from database.types import Conditions

def get_all_products() -> Sequence[Product] | None:
    session = SessionLocal()
    
    try: 
        products = session.scalars(select(Product)).all()
        return products
    except Exception:
        return None
    finally:
        session.close()
    
def get_products_by_condition(conditions: list[Conditions]) -> Sequence[Product] | None :
    session = SessionLocal()
    condition_list = []

    for condition in conditions:
        column = getattr(Product, condition.key, None)
        if column is None:
            return None
        
        if not isinstance(condition.value, column.type.python_type):
            return None
        
        operation = condition.getOperation()
        if operation is None:
            return None
        
        con = operation(column, condition.value)
        condition_list.append(con)
        
    products = session.scalars(select(Product).where(*condition_list)).all()
    return products
