from datetime import date

from sqlalchemy import(
    Integer,
    String,
    Float,
    Date,
    ForeignKey,
    Table,
    Column
)

from sqlalchemy.orm import(
    Mapped,
    mapped_column,
    relationship,
)

from database.database import Base


promotion_products = Table(
    "promotion_products",
    Base.metadata,
    Column("promotion_id", ForeignKey("promotions.promotion_id")),
    Column("product_id", ForeignKey("products.product_id")),
)


class Product(Base):

    __tablename__ = "products"

    product_id :Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    product_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    product_description: Mapped[str | None] = mapped_column(
        String(200),
    )

    product_brand: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    product_category: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    product_price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    product_stock: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    last_fulfillment:Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    next_fulfillment: Mapped[date | None] = mapped_column(
        Date
    )

    promotions: Mapped[list["Promotion"]] = relationship(
        secondary=promotion_products,
        back_populates="target_products"
    )

    fulfillments: Mapped[list["Fulfillments"]] = relationship(
        back_populates="product"
    )

    sales: Mapped[list["Sale"]] = relationship(
        back_populates="product"
    )


    
class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    customer_age: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )

    customer_gender: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    customer_ethnicity: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    
    ethnicity: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    sales: Mapped[list["Sale"]] = relationship(
        back_populates="customer"
    )


class Fulfillments(Base):
    __tablename__ = "fulfillments"

    fullfilment_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.product_id"),
        nullable=False,
    )

    fullfiliment_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )
    
    fullfillment_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    product: Mapped["Product"] = relationship(
        back_populates="fulfillments"
    )

class Promotion(Base):
    __tablename__ = "promotions"

    promotion_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    promotion_name: Mapped[str] = mapped_column(
        String(100)
    )

    promotion_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    discount_percent: Mapped[int | None] = mapped_column(
        Integer
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    end_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    target_products: Mapped[list["Product"]] = relationship(
        secondary=promotion_products,
        back_populates="promotions"
    )

    sales: Mapped[list["Sale"]] = relationship(
        back_populates="promotion"
    )

class Sale(Base):
    __tablename__ = "sales"

    sale_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.product_id"),
        nullable=False
    )

    quantity_sold: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    regular_price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    sale_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    promotion_id: Mapped[int | None] = mapped_column(
        ForeignKey("promotions.promotion_id")
    )

    final_price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.customer_id"),
        nullable=False
    )

    product: Mapped["Product"] = relationship(
        back_populates="sales"
    )

    promotion: Mapped["Promotion"] = relationship(
        back_populates="sales"
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="sales"
    )

