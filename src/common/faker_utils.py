"""
Project     : GlobalMart Enterprise Lakehouse
Module      : Faker Utilities
Author      : Ambuj Kumar
Description : Enterprise reusable Faker utility methods for synthetic
              data generation.
"""

from __future__ import annotations

import random
import string
from datetime import date, datetime, timedelta
from decimal import Decimal

from faker import Faker

# ==========================================================
# Faker Initialization
# ==========================================================

FAKER_SEED = 42

fake = Faker()

Faker.seed(FAKER_SEED)
random.seed(FAKER_SEED)

# ==========================================================
# Constants
# ==========================================================

GENDERS = (
    "Male",
    "Female",
    "Other",
)

LOYALTY_TIERS = (
    "Bronze",
    "Silver",
    "Gold",
    "Platinum",
)

PAYMENT_METHODS = (
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Wallet",
    "Cash",
)

ORDER_STATUS = (
    "Pending",
    "Confirmed",
    "Packed",
    "Shipped",
    "Delivered",
    "Cancelled",
)

SHIPMENT_STATUS = (
    "Created",
    "Dispatched",
    "In Transit",
    "Out For Delivery",
    "Delivered",
)

COUNTRIES = (
    "India",
    "USA",
    "Canada",
    "Germany",
    "United Kingdom",
    "Australia",
    "Singapore",
    "Japan",
)

CURRENCIES = (
    "INR",
    "USD",
    "EUR",
    "GBP",
    "JPY",
)

EMAIL_DOMAINS = (
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
)

# ==========================================================
# Faker Utility Class
# ==========================================================


class FakerUtils:
    """
    Enterprise reusable faker utility methods.
    """

    # ======================================================
    # Customer / Person
    # ======================================================

    @staticmethod
    def customer_name() -> str:
        """Generate customer name."""
        return fake.name()

    @staticmethod
    def first_name() -> str:
        """Generate first name."""
        return fake.first_name()

    @staticmethod
    def last_name() -> str:
        """Generate last name."""
        return fake.last_name()

    @staticmethod
    def gender() -> str:
        """Generate gender."""
        return random.choice(GENDERS)

    @staticmethod
    def date_of_birth(
        minimum_age: int = 18,
        maximum_age: int = 75,
    ) -> date:
        """Generate date of birth."""
        return fake.date_of_birth(
            minimum_age=minimum_age,
            maximum_age=maximum_age,
        )

    @staticmethod
    def email() -> str:
        """Generate email address."""
        username = (
            fake.first_name() + "." + fake.last_name()
        ).lower()

        return (
            f"{username}"
            f"{random.randint(1,999)}"
            f"@{random.choice(EMAIL_DOMAINS)}"
        )

    @staticmethod
    def phone() -> str:
        """Generate phone number."""
        return fake.phone_number()

    @staticmethod
    def customer_id() -> str:
        """Generate customer identifier."""
        return f"CUST{random.randint(100000,999999)}"

    # ======================================================
    # Address
    # ======================================================

    @staticmethod
    def address() -> str:
        """Generate address."""
        return fake.address().replace("\n", ", ")

    @staticmethod
    def city() -> str:
        """Generate city."""
        return fake.city()

    @staticmethod
    def state() -> str:
        """Generate state."""
        return fake.state()

    @staticmethod
    def country() -> str:
        """Generate country."""
        return random.choice(COUNTRIES)

    @staticmethod
    def postal_code() -> str:
        """Generate postal code."""
        return fake.postcode()

    # ======================================================
    # Company
    # ======================================================

    @staticmethod
    def company() -> str:
        """Generate company name."""
        return fake.company()

    @staticmethod
    def company_email() -> str:
        """Generate company email."""
        company = (
            fake.company()
            .replace(",", "")
            .replace(".", "")
            .replace(" ", "")
            .lower()
        )

        return (
            f"info@{company}.com"
        )

    @staticmethod
    def company_phone() -> str:
        """Generate company phone."""
        return fake.phone_number()

    @staticmethod
    def website() -> str:
        """Generate website."""
        company = (
            fake.company()
            .replace(",", "")
            .replace(".", "")
            .replace(" ", "")
            .lower()
        )

        return f"https://www.{company}.com"

    # ======================================================
    # Common Random Values
    # ======================================================

    @staticmethod
    def boolean() -> bool:
        """Generate boolean."""
        return random.choice([True, False])

    @staticmethod
    def percentage(
        minimum: int = 0,
        maximum: int = 100,
    ) -> float:
        """Generate percentage."""
        return round(
            random.uniform(minimum, maximum),
            2,
        )

    @staticmethod
    def quantity(
        minimum: int = 1,
        maximum: int = 100,
    ) -> int:
        """Generate quantity."""
        return random.randint(
            minimum,
            maximum,
        )

    @staticmethod
    def price(
        minimum: float = 10.0,
        maximum: float = 10000.0,
    ) -> Decimal:
        """Generate price."""
        return Decimal(
            str(
                round(
                    random.uniform(
                        minimum,
                        maximum,
                    ),
                    2,
                )
            )
        )

    # ======================================================
    # Date & Time
    # ======================================================

    @staticmethod
    def current_timestamp() -> datetime:
        """Generate current timestamp."""
        return datetime.now()

    @staticmethod
    def random_date(
        start_days: int = -365,
        end_days: int = 0,
    ) -> datetime:
        """
        Generate random date within range.
        """
        today = datetime.now()

        return today + timedelta(
            days=random.randint(
                start_days,
                end_days,
            )
        )

    # ======================================================
    # Text
    # ======================================================

    @staticmethod
    def random_sentence(
        words: int = 8,
    ) -> str:
        """Generate random sentence."""
        return fake.sentence(
            nb_words=words
        )

    @staticmethod
    def random_paragraph() -> str:
        """Generate paragraph."""
        return fake.paragraph()

    # ======================================================
    # Identifiers
    # ======================================================

    @staticmethod
    def uuid() -> str:
        """Generate UUID."""
        return fake.uuid4()

    @staticmethod
    def random_string(
        length: int = 10,
    ) -> str:
        """Generate random string."""
        return "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=length,
            )
        )

        # ======================================================
    # Supplier
    # ======================================================

    @staticmethod
    def supplier_name() -> str:
        """Generate supplier company name."""
        return fake.company()

    @staticmethod
    def supplier_code() -> str:
        """Generate supplier code."""
        return f"SUP{random.randint(100000, 999999)}"

    @staticmethod
    def supplier_id() -> str:
        """Generate supplier ID."""
        return f"SUPP{random.randint(100000, 999999)}"

    @staticmethod
    def tax_number() -> str:
        """Generate GST/VAT number."""
        return f"GSTIN{random.randint(1000000000, 9999999999)}"

    @staticmethod
    def business_registration_number() -> str:
        """Generate business registration number."""
        return f"REG{random.randint(10000000,99999999)}"

    # ======================================================
    # Warehouse
    # ======================================================

    @staticmethod
    def warehouse_id() -> str:
        """Generate warehouse ID."""
        return f"WH{random.randint(1000,9999)}"

    @staticmethod
    def warehouse_code() -> str:
        """Generate warehouse code."""
        return (
            "WH-"
            + "".join(
                random.choices(
                    string.ascii_uppercase,
                    k=3,
                )
            )
            + "-"
            + str(random.randint(100,999))
        )

    @staticmethod
    def warehouse_name() -> str:
        """Generate warehouse name."""
        return (
            random.choice(
                [
                    "North",
                    "South",
                    "East",
                    "West",
                    "Central",
                ]
            )
            + " Distribution Center"
        )

    @staticmethod
    def warehouse_capacity() -> int:
        """Generate warehouse capacity."""
        return random.randint(
            5000,
            50000,
        )

    # ======================================================
    # Product
    # ======================================================

    @staticmethod
    def product_id() -> str:
        """Generate product ID."""
        return f"PRD{random.randint(100000,999999)}"

    @staticmethod
    def sku() -> str:
        """Generate SKU."""
        return (
            "SKU-"
            + "".join(
                random.choices(
                    string.ascii_uppercase,
                    k=3,
                )
            )
            + "-"
            + str(random.randint(100000,999999))
        )

    @staticmethod
    def brand_name() -> str:
        """Generate brand name."""
        return random.choice(
            [
                "Apple",
                "Samsung",
                "Sony",
                "LG",
                "Nike",
                "Adidas",
                "Nestle",
                "ITC",
                "Puma",
                "Lenovo",
                "HP",
                "Dell",
                "Philips",
                "Boat",
                "Amul",
            ]
        )

    @staticmethod
    def product_name() -> str:
        """Generate product name."""
        adjective = random.choice(
            [
                "Premium",
                "Classic",
                "Advanced",
                "Smart",
                "Organic",
                "Eco",
                "Portable",
                "Wireless",
                "Professional",
                "Luxury",
            ]
        )

        noun = random.choice(
            [
                "Phone",
                "Laptop",
                "Bottle",
                "Chair",
                "Desk",
                "Television",
                "Watch",
                "Shoes",
                "Bag",
                "Speaker",
                "Keyboard",
                "Mouse",
                "Monitor",
            ]
        )

        return f"{adjective} {noun}"

    @staticmethod
    def product_description() -> str:
        """Generate product description."""
        return fake.text(
            max_nb_chars=120,
        )

    @staticmethod
    def product_weight() -> float:
        """Generate product weight."""
        return round(
            random.uniform(
                0.1,
                25.0,
            ),
            2,
        )

    @staticmethod
    def product_price() -> Decimal:
        """Generate selling price."""
        return Decimal(
            str(
                round(
                    random.uniform(
                        50,
                        50000,
                    ),
                    2,
                )
            )
        )

    @staticmethod
    def product_cost() -> Decimal:
        """Generate product cost."""
        return Decimal(
            str(
                round(
                    random.uniform(
                        25,
                        35000,
                    ),
                    2,
                )
            )
        )

    # ======================================================
    # Inventory
    # ======================================================

    @staticmethod
    def stock_quantity() -> int:
        """Generate stock quantity."""
        return random.randint(
            0,
            5000,
        )

    @staticmethod
    def reorder_level() -> int:
        """Generate reorder level."""
        return random.randint(
            25,
            500,
        )

    @staticmethod
    def inventory_status() -> str:
        """Generate inventory status."""
        return random.choice(
            [
                "In Stock",
                "Low Stock",
                "Out Of Stock",
                "Reserved",
            ]
        )

    # ======================================================
    # Payment
    # ======================================================

    @staticmethod
    def payment_id() -> str:
        """Generate payment ID."""
        return f"PAY{random.randint(1000000,9999999)}"

    @staticmethod
    def payment_method() -> str:
        """Generate payment method."""
        return random.choice(
            PAYMENT_METHODS
        )

    @staticmethod
    def transaction_reference() -> str:
        """Generate transaction reference."""
        return (
            "TXN"
            + datetime.now().strftime("%Y%m%d")
            + str(
                random.randint(
                    100000,
                    999999,
                )
            )
        )

    @staticmethod
    def payment_status() -> str:
        """Generate payment status."""
        return random.choice(
            [
                "Pending",
                "Completed",
                "Failed",
                "Refunded",
                "Cancelled",
            ]
        )

    # ======================================================
    # Shipment
    # ======================================================

    @staticmethod
    def shipment_id() -> str:
        """Generate shipment ID."""
        return f"SHP{random.randint(1000000,9999999)}"

    @staticmethod
    def tracking_number() -> str:
        """Generate shipment tracking number."""
        return (
            "TRK"
            + "".join(
                random.choices(
                    string.ascii_uppercase,
                    k=4,
                )
            )
            + str(
                random.randint(
                    100000,
                    999999,
                )
            )
        )

    @staticmethod
    def courier_name() -> str:
        """Generate courier company."""
        return random.choice(
            [
                "BlueDart",
                "Delhivery",
                "DTDC",
                "FedEx",
                "UPS",
                "DHL",
                "XpressBees",
                "India Post",
            ]
        )

    @staticmethod
    def shipment_status() -> str:
        """Generate shipment status."""
        return random.choice(
            SHIPMENT_STATUS
        )

    @staticmethod
    def shipping_cost() -> Decimal:
        """Generate shipping cost."""
        return Decimal(
            str(
                round(
                    random.uniform(
                        50,
                        1500,
                    ),
                    2,
                )
            )
        )
    
        # ======================================================
    # Orders
    # ======================================================

    @staticmethod
    def order_id() -> str:
        """Generate order ID."""
        return f"ORD{random.randint(10000000, 99999999)}"

    @staticmethod
    def order_number() -> str:
        """Generate order number."""
        return (
            "GM-"
            + datetime.now().strftime("%Y%m%d")
            + "-"
            + str(random.randint(100000, 999999))
        )

    @staticmethod
    def order_status() -> str:
        """Generate order status."""
        return random.choice(ORDER_STATUS)

    @staticmethod
    def order_date(
        start_days: int = -365,
        end_days: int = 0,
    ) -> datetime:
        """Generate order date."""
        return FakerUtils.random_date(
            start_days,
            end_days,
        )

    # ======================================================
    # Customer Reviews
    # ======================================================

    @staticmethod
    def review_id() -> str:
        """Generate review ID."""
        return f"REV{random.randint(1000000,9999999)}"

    @staticmethod
    def review_rating() -> int:
        """Generate review rating."""
        return random.randint(1, 5)

    @staticmethod
    def review_title() -> str:
        """Generate review title."""
        return random.choice(
            [
                "Excellent Product",
                "Highly Recommended",
                "Good Value",
                "Average Experience",
                "Not Worth the Price",
                "Satisfied Purchase",
                "Amazing Quality",
                "Will Buy Again",
            ]
        )

    @staticmethod
    def review_comment() -> str:
        """Generate review comment."""
        return fake.paragraph(
            nb_sentences=3,
        )

    # ======================================================
    # Returns
    # ======================================================

    @staticmethod
    def return_id() -> str:
        """Generate return ID."""
        return f"RET{random.randint(1000000,9999999)}"

    @staticmethod
    def return_reason() -> str:
        """Generate return reason."""
        return random.choice(
            [
                "Damaged Item",
                "Wrong Product",
                "Defective Product",
                "Quality Issue",
                "Late Delivery",
                "Customer Changed Mind",
                "Incorrect Size",
                "Duplicate Order",
            ]
        )

    @staticmethod
    def refund_status() -> str:
        """Generate refund status."""
        return random.choice(
            [
                "Pending",
                "Approved",
                "Rejected",
                "Processed",
            ]
        )

    # ======================================================
    # Loyalty
    # ======================================================

    @staticmethod
    def loyalty_id() -> str:
        """Generate loyalty ID."""
        return f"LOY{random.randint(1000000,9999999)}"

    @staticmethod
    def loyalty_tier() -> str:
        """Generate loyalty tier."""
        return random.choice(LOYALTY_TIERS)

    @staticmethod
    def loyalty_points() -> int:
        """Generate loyalty points."""
        return random.randint(
            0,
            50000,
        )

    # ======================================================
    # Promotions
    # ======================================================

    @staticmethod
    def promotion_id() -> str:
        """Generate promotion ID."""
        return f"PROMO{random.randint(10000,99999)}"

    @staticmethod
    def promotion_code() -> str:
        """Generate promotion code."""
        return (
            "SAVE"
            + str(random.randint(10, 99))
        )

    @staticmethod
    def discount_percentage() -> float:
        """Generate discount percentage."""
        return round(
            random.uniform(
                5,
                70,
            ),
            2,
        )

    @staticmethod
    def coupon_code() -> str:
        """Generate coupon code."""
        return (
            "".join(
                random.choices(
                    string.ascii_uppercase,
                    k=4,
                )
            )
            + str(
                random.randint(
                    100,
                    999,
                )
            )
        )

    # ======================================================
    # Finance
    # ======================================================

    @staticmethod
    def currency() -> str:
        """Generate currency."""
        return random.choice(CURRENCIES)

    @staticmethod
    def tax_percentage() -> float:
        """Generate tax percentage."""
        return round(
            random.uniform(
                5,
                28,
            ),
            2,
        )

    @staticmethod
    def exchange_rate() -> Decimal:
        """Generate exchange rate."""
        return Decimal(
            str(
                round(
                    random.uniform(
                        0.5,
                        100,
                    ),
                    4,
                )
            )
        )

    # ======================================================
    # Employee
    # ======================================================

    @staticmethod
    def employee_id() -> str:
        """Generate employee ID."""
        return f"EMP{random.randint(100000,999999)}"

    @staticmethod
    def employee_designation() -> str:
        """Generate employee designation."""
        return random.choice(
            [
                "Store Manager",
                "Sales Executive",
                "Cashier",
                "Warehouse Executive",
                "Delivery Associate",
                "HR Executive",
                "Finance Analyst",
                "Data Engineer",
                "Software Engineer",
                "Operations Manager",
            ]
        )

    @staticmethod
    def department() -> str:
        """Generate department."""
        return random.choice(
            [
                "Sales",
                "Finance",
                "IT",
                "Operations",
                "HR",
                "Marketing",
                "Supply Chain",
                "Customer Service",
            ]
        )

    # ======================================================
    # Miscellaneous
    # ======================================================

    @staticmethod
    def country_code() -> str:
        """Generate ISO country code."""
        return fake.country_code()

    @staticmethod
    def latitude() -> float:
        """Generate latitude."""
        return float(fake.latitude())

    @staticmethod
    def longitude() -> float:
        """Generate longitude."""
        return float(fake.longitude())

    @staticmethod
    def ip_address() -> str:
        """Generate IPv4 address."""
        return fake.ipv4()

    @staticmethod
    def mac_address() -> str:
        """Generate MAC address."""
        return fake.mac_address()

    @staticmethod
    def file_name(extension: str = "csv") -> str:
        """Generate file name."""
        return (
            fake.file_name(
                extension=extension
            )
        )

    @staticmethod
    def image_url() -> str:
        """Generate image URL."""
        return fake.image_url()

    @staticmethod
    def user_agent() -> str:
        """Generate user agent."""
        return fake.user_agent()

    @staticmethod
    def color() -> str:
        """Generate color."""
        return fake.color_name()


__all__ = [
    "FakerUtils",
]