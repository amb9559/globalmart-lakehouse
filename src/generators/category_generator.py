"""
---------------------------------------------------------
Project : GlobalMart Enterprise Lakehouse
Module  : category_generator.py
Purpose : Generate Category Master Data
Author  : GlobalMart Data Engineering Team
---------------------------------------------------------
"""

from datetime import datetime
from typing import List, Dict
import random

from src.utils.faker_utils import FakerUtils


class CategoryGenerator:
    """
    Generates Product Category Master data.
    """

    CATEGORY_DATA = {
        "Electronics": [
            "Mobile Phones",
            "Laptops",
            "Televisions",
            "Audio",
            "Cameras"
        ],
        "Fashion": [
            "Men Clothing",
            "Women Clothing",
            "Kids Clothing",
            "Footwear",
            "Accessories"
        ],
        "Home & Kitchen": [
            "Furniture",
            "Kitchen Appliances",
            "Home Decor",
            "Storage",
            "Lighting"
        ],
        "Beauty": [
            "Skincare",
            "Hair Care",
            "Makeup",
            "Fragrances"
        ],
        "Sports": [
            "Fitness",
            "Outdoor",
            "Cycling",
            "Sports Equipment"
        ],
        "Books": [
            "Fiction",
            "Non-Fiction",
            "Education",
            "Comics"
        ],
        "Grocery": [
            "Beverages",
            "Snacks",
            "Dairy",
            "Frozen Foods",
            "Bakery"
        ],
        "Toys": [
            "Educational",
            "Action Figures",
            "Board Games",
            "Puzzles"
        ]
    }

    @classmethod
    def generate(cls) -> List[Dict]:
        """
        Generate category records.

        Returns:
            List[Dict]
        """

        categories = []
        category_id = 1001
        subcategory_id = 5001

        current_timestamp = datetime.utcnow().isoformat()

        for category_name, subcategories in cls.CATEGORY_DATA.items():

            category_record = {
                "category_id": category_id,
                "category_name": category_name,
                "parent_category_id": None,
                "category_level": 1,
                "description": f"{category_name} Category",
                "is_active": True,
                "created_date": current_timestamp,
                "updated_date": current_timestamp
            }

            categories.append(category_record)

            parent_id = category_id
            category_id += 1

            for subcategory in subcategories:

                subcategory_record = {
                    "category_id": subcategory_id,
                    "category_name": subcategory,
                    "parent_category_id": parent_id,
                    "category_level": 2,
                    "description": f"{subcategory} Products",
                    "is_active": random.choice(
                        [
                            True,
                            True,
                            True,
                            True,
                            False
                        ]
                    ),
                    "created_date": current_timestamp,
                    "updated_date": current_timestamp
                }

                categories.append(subcategory_record)

                subcategory_id += 1

        return categories

    @staticmethod
    def generate_random_categories(count: int) -> List[Dict]:
        """
        Generate additional random categories.

        Args:
            count: Number of categories.

        Returns:
            List[Dict]
        """

        categories = []

        for index in range(count):

            categories.append(
                {
                    "category_id": 100000 + index,
                    "category_name": FakerUtils.company(),
                    "parent_category_id": None,
                    "category_level": 1,
                    "description": FakerUtils.random_sentence(),
                    "is_active": FakerUtils.boolean(),
                    "created_date": datetime.utcnow().isoformat(),
                    "updated_date": datetime.utcnow().isoformat()
                }
            )

        return categories


if __name__ == "__main__":

    records = CategoryGenerator.generate()

    print(f"Generated {len(records)} category records.\n")

    for record in records[:10]:
        print(record)