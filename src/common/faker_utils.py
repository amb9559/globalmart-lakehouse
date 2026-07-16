"""
---------------------------------------------------------
Project : GlobalMart Enterprise Lakehouse
Module  : faker_utils.py
Purpose : Generate synthetic enterprise data
Author  : GlobalMart Data Engineering Team
---------------------------------------------------------
"""

import random
import uuid
from datetime import timedelta

from faker import Faker

fake = Faker()


class FakerUtils:
    """
    Utility class for generating synthetic enterprise data.
    """

    @staticmethod
    def uuid() -> str:
        """Generate UUID."""

        return str(uuid.uuid4())

    @staticmethod
    def first_name() -> str:
        return fake.first_name()

    @staticmethod
    def last_name() -> str:
        return fake.last_name()

    @staticmethod
    def full_name() -> str:
        return fake.name()

    @staticmethod
    def email() -> str:
        return fake.email().lower()

    @staticmethod
    def phone_number() -> str:
        return fake.msisdn()[:10]

    @staticmethod
    def address() -> str:
        return fake.street_address()

    @staticmethod
    def city() -> str:
        return fake.city()

    @staticmethod
    def state() -> str:
        return fake.state()

    @staticmethod
    def country() -> str:
        return fake.country()

    @staticmethod
    def postal_code() -> str:
        return fake.postcode()

    @staticmethod
    def company() -> str:
        return fake.company()

    @staticmethod
    def job_title() -> str:
        return fake.job()

    @staticmethod
    def date_of_birth(min_age: int = 18, max_age: int = 70):
        return fake.date_of_birth(
            minimum_age=min_age,
            maximum_age=max_age
        )

    @staticmethod
    def random_date(start_days: int = -3650, end_days: int = 0):
        """
        Generate random date within a range.
        """

        start = fake.date_time_between(
            start_date=f"{start_days}d",
            end_date=f"{end_days}d"
        )

        return start.date()

    @staticmethod
    def random_datetime(start_days: int = -3650, end_days: int = 0):
        """
        Generate random datetime.
        """

        return fake.date_time_between(
            start_date=f"{start_days}d",
            end_date=f"{end_days}d"
        )

    @staticmethod
    def random_timestamp():
        return fake.date_time_this_decade()

    @staticmethod
    def gender():
        return random.choice(
            [
                "Male",
                "Female",
                "Other"
            ]
        )

    @staticmethod
    def loyalty_tier():
        return random.choice(
            [
                "Bronze",
                "Silver",
                "Gold",
                "Platinum"
            ]
        )

    @staticmethod
    def payment_method():
        return random.choice(
            [
                "Credit Card",
                "Debit Card",
                "UPI",
                "Wallet",
                "Net Banking",
                "Cash"
            ]
        )

    @staticmethod
    def order_status():
        return random.choice(
            [
                "Pending",
                "Processing",
                "Shipped",
                "Delivered",
                "Cancelled",
                "Returned"
            ]
        )

    @staticmethod
    def shipment_status():
        return random.choice(
            [
                "Packed",
                "Dispatched",
                "In Transit",
                "Delivered",
                "Delayed"
            ]
        )

    @staticmethod
    def review_rating():
        return random.randint(1, 5)

    @staticmethod
    def quantity(min_qty: int = 1, max_qty: int = 10):
        return random.randint(min_qty, max_qty)

    @staticmethod
    def price(min_price: float = 10.0, max_price: float = 5000.0):
        return round(random.uniform(min_price, max_price), 2)

    @staticmethod
    def percentage(min_value: int = 0, max_value: int = 100):
        return random.randint(min_value, max_value)

    @staticmethod
    def boolean():
        return random.choice([True, False])

    @staticmethod
    def future_date(days: int = 30):
        return fake.date_between(
            start_date="today",
            end_date=f"+{days}d"
        )

    @staticmethod
    def past_date(days: int = 365):
        return fake.date_between(
            start_date=f"-{days}d",
            end_date="today"
        )

    @staticmethod
    def random_sentence(words: int = 8):
        return fake.sentence(nb_words=words)

    @staticmethod
    def random_paragraph(sentences: int = 3):
        return fake.paragraph(nb_sentences=sentences)

    @staticmethod
    def sku():
        return f"SKU-{random.randint(100000, 999999)}"

    @staticmethod
    def product_code():
        return f"PRD-{random.randint(10000, 99999)}"

    @staticmethod
    def warehouse_code():
        return f"WH-{random.randint(100,999)}"

    @staticmethod
    def employee_id():
        return f"EMP-{random.randint(100000,999999)}"

    @staticmethod
    def customer_id():
        return f"CUST-{random.randint(10000000,99999999)}"

    @staticmethod
    def supplier_id():
        return f"SUP-{random.randint(10000,99999)}"

    @staticmethod
    def order_id():
        return f"ORD-{random.randint(100000000,999999999)}"

    @staticmethod
    def payment_id():
        return f"PAY-{random.randint(100000000,999999999)}"

    @staticmethod
    def shipment_id():
        return f"SHP-{random.randint(100000000,999999999)}"

    @staticmethod
    def promotion_code():
        return f"PROMO-{random.randint(1000,9999)}"