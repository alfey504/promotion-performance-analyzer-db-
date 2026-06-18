from database.database import SessionLocal
from database.models import Product
from database import product_db
from database.create_table import init_tables
from database.types import Conditions

def main():
    print("Hello from db-setup!")
    init_tables()
    # get_data()
    # 
    get_product_caluse()

def get_product_caluse():
    condition = Conditions[int]("product_id", 2, "==")
    products = product_db.get_products_by_condition(list({condition}))
    for product in products:
        print(product.product_name)

def get_data():
    session = SessionLocal()
    
    try:
        product = Product(
            product_name="iPhone 16",
            product_description="Latest Apple smartphone",
            product_brand="Apple",
            product_category="Electronics",
            product_stock=100,
            product_price=200,
            last_fulfillment="2026-06-15",
            next_fulfillment="2026-07-01"
        )

        session.add(product)
        session.commit()

        print(f"Inserted product with ID: {product.product_id}")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()

if __name__ == "__main__":
    main()
