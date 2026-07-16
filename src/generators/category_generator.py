"""
Project     : GlobalMart Enterprise Lakehouse
Module      : Category Generator
Author      : Ambuj Kumar
Description : Generates category master data.
"""

from __future__ import annotations

from datetime import UTC, datetime

import pandas as pd

from .base_generator import BaseGenerator


CATEGORY_DATA = {
    "Electronics": [
        "Mobile Phones",
        "Laptops",
        "Televisions",
        "Audio",
        "Cameras",
    ],
    "Fashion": [
        "Men Clothing",
        "Women Clothing",
        "Kids Clothing",
        "Footwear",
        "Accessories",
    ],
    "Home & Kitchen": [
        "Furniture",
        "Kitchen Appliances",
        "Home Decor",
        "Storage",
        "Lighting",
    ],
    "Beauty": [
        "Skincare",
        "Hair Care",
        "Makeup",
        "Fragrances",
    ],
    "Sports": [
        "Fitness",
        "Outdoor",
        "Cycling",
        "Sports Equipment",
    ],
    "Books": [
        "Fiction",
        "Non-Fiction",
        "Education",
        "Comics",
    ],
    "Grocery": [
        "Beverages",
        "Snacks",
        "Dairy",
        "Frozen Foods",
        "Bakery",
    ],
    "Toys": [
        "Educational",
        "Action Figures",
        "Board Games",
        "Puzzles",
    ],
}


class CategoryGenerator(BaseGenerator):
    """
    Enterprise category generator.
    """

    def __init__(self):
        super().__init__("categories")

    def generate(self) -> pd.DataFrame:

        records = []

        category_id = 1001
        subcategory_id = 5001

        timestamp = datetime.now(UTC)

        for category, subcategories in CATEGORY_DATA.items():

            records.append(
                {
                    "category_id": category_id,
                    "category_name": category,
                    "parent_category_id": None,
                    "category_level": 1,
                    "description": f"{category} Category",
                    "is_active": True,
                    "created_timestamp": timestamp,
                    "updated_timestamp": timestamp,
                    "batch_id": self.batch_id,
                }
            )

            parent_id = category_id
            category_id += 1

            for subcategory in subcategories:

                records.append(
                    {
                        "category_id": subcategory_id,
                        "category_name": subcategory,
                        "parent_category_id": parent_id,
                        "category_level": 2,
                        "description": f"{subcategory} Products",
                        "is_active": True,
                        "created_timestamp": timestamp,
                        "updated_timestamp": timestamp,
                        "batch_id": self.batch_id,
                    }
                )

                subcategory_id += 1

        return pd.DataFrame(records)


if __name__ == "__main__":

    generator = CategoryGenerator()

    df = generator.run()

    print(df.head())