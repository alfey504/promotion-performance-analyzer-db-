
from database.database import SessionLocal
from database.models import Product, Promotion
from database import product_db, promotion_db
from database.create_table import init_tables
from database.utils import Conditions 
from get_random_product import get_product
import random
from datetime import date, timedelta

def main():

    print("Hello from db-setup!")
    init_tables()
    # get_data()
    # 
    # get_product_caluse()
    # make_dummy_promotions_table(100)
    
def price_sum(): 
    try:  
        result = product_db.get_total_inventory_price()
        print(result)
    except Exception as e:
        print(e)
    

def get_product_caluse():
    condition = Conditions[int]("product_id", 2, "==")
    try:
        products = product_db.get_products_by_condition(list({condition}))
        for product in products:
            print(product.product_name)
    except Exception as e:
        print(e)
    

def make_dummy_products():
    session = SessionLocal()

    try:
        products = get_product()

        session.add_all(products)
        session.commit()

        print(f"Inserted all products successfully")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()

def make_dummy_promotions(products: list[Product], start_date: date, end_date: date):
    promotion_types = ["sale", "buy_1_get_1", "cashback"]
    promotion_name = [
        ["summer sales", "winter sales", "spring sale", "autum sale", "christmas sale"],
        ["heatwave bonanza", "winter wonderland", "spring fest", "autum bloom", "santas blessing"],
        ["sunny paybacks", "frosty surprise", "blooming saves", "bolomeht saveth", "santas cometh"]
    ]

    promo_type_index = random.randint(0,2)
    sale_season_index = random.randint(0,4)

    dummy_promotion = Promotion(
        promotion_name=promotion_name[promo_type_index][sale_season_index],
        promotion_type=promotion_types[promo_type_index],
        discount_percent=random.randint(10, 50),
        start_date=start_date,
        end_date=end_date,

        # assuming these Product objects already exist
        target_products=products,

        # optional sales relationship
        sales=[]
    )
    return dummy_promotion
    
def make_dummy_promotions_table(count: int):
    products = product_db.get_all_products()
    product_id_range = range(4, 58)
    start_date = date(2004, 3, 1)

    promotions: list[Promotion] = []
    for i in range(0, count):
        sample = random.sample(product_id_range, random.randint(10, 15))
        sample_set = set(sample)
        filtered_products = [p for p in products if p.product_id in sample_set]
        sale_duration = random.choice([7, 14, 30])
        end_date = start_date + timedelta(sale_duration)
        promotion = make_dummy_promotions(products=filtered_products, start_date=start_date, end_date=end_date)
        promotions.append(promotion)
    
    promotion_db.insert_promotoion_batch(promotions=promotions)

def get_random_set_of_product_id():
    num_pool = range(4, 58)
    return random.sample(num_pool, random.randint(10,15))


if __name__ == "__main__":
    main()
