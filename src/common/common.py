"""
Project     : GlobalMart Enterprise Lakehouse
Module      : Common Utilities
Author      : Ambuj Kumar
Description : Common reusable utility functions for the enterprise
              data generation framework.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Optional
from uuid import uuid4

import pandas as pd

from .logger import get_logger

logger = get_logger(__name__)


# ==========================================================
# Common Utility Class
# ==========================================================


class CommonUtils:
    """
    Common reusable utility methods.
    """

    @staticmethod
    def create_directory(directory: Path) -> None:
        """
        Create directory if it does not exist.
        """
        directory.mkdir(parents=True, exist_ok=True)
        logger.info("Directory verified: %s", directory)

    @staticmethod
    def generate_batch_id() -> str:
        """
        Generate a unique batch ID.
        """
        return datetime.now().strftime("%Y%m%d%H%M%S")

    @staticmethod
    def current_timestamp() -> str:
        """
        Return current timestamp.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def generate_uuid() -> str:
        """
        Generate a UUID.
        """
        return str(uuid4())

    @staticmethod
    def file_exists(file_path: Path) -> bool:
        """
        Check whether a file exists.
        """
        return file_path.exists()

    @staticmethod
    def delete_file(file_path: Path) -> None:
        """
        Delete a file if it exists.
        """
        if file_path.exists():
            file_path.unlink()
            logger.info("Deleted file: %s", file_path)

    @staticmethod
    def validate_dataframe(df: pd.DataFrame) -> None:
        """
        Validate a Pandas DataFrame.
        """
        if df is None:
            raise ValueError("DataFrame is None.")

        if df.empty:
            raise ValueError("DataFrame is empty.")

    @staticmethod
    def save_csv(
        df: pd.DataFrame,
        output_path: Path,
        file_name: str,
    ) -> None:
        """
        Save DataFrame as CSV.
        """
        CommonUtils.create_directory(output_path)

        file_path = output_path / f"{file_name}.csv"

        df.to_csv(
            file_path,
            index=False,
        )

        logger.info("CSV saved: %s", file_path)

    @staticmethod
    def save_json(
        df: pd.DataFrame,
        output_path: Path,
        file_name: str,
    ) -> None:
        """
        Save DataFrame as JSON.
        """
        CommonUtils.create_directory(output_path)

        file_path = output_path / f"{file_name}.json"

        df.to_json(
            file_path,
            orient="records",
            indent=4,
        )

        logger.info("JSON saved: %s", file_path)

    @staticmethod
    def save_parquet(
        df: pd.DataFrame,
        output_path: Path,
        file_name: str,
    ) -> None:
        """
        Save DataFrame as Parquet.
        """
        CommonUtils.create_directory(output_path)

        file_path = output_path / f"{file_name}.parquet"

        df.to_parquet(
            file_path,
            index=False,
        )

        logger.info("Parquet saved: %s", file_path)

    @staticmethod
    def output_file_name(
        dataset_name: str,
        suffix: Optional[str] = None,
    ) -> str:
        """
        Generate standardized output file name.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if suffix:
            return f"{dataset_name}_{suffix}_{timestamp}"

        return f"{dataset_name}_{timestamp}"


__all__ = [
    "CommonUtils",
]