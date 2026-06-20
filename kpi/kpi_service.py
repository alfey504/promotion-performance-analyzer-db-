from database import promotion_db
from database.models import Promotion
def get_sales_before_and_during_promotion(id: int):
    promotion: Promotion | None
    try:
        promotion = promotion_db.get_promotion_by_id(id)
        if promotion is None:
            return None
        print(promotion.target_products)
    except Exception as e:
        raise e
    
 