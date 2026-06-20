from database.database import SessionLocal
from sqlalchemy import select
from database.models import Promotion

def get_promotion_by_id(promotion_id: int) -> Promotion:
    session = SessionLocal()
    try:
        stmt = select(Promotion).where(Promotion.promotion_id == promotion_id)
        result = session.scalar(stmt)
        return result
    except Exception as e:
        raise e
    finally:
        session.close()

def insert_promotoion_batch(promotions: list[Promotion]):
    session = SessionLocal()
    try:
        session.add_all(promotions)
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()