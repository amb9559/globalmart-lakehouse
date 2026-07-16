"""
Project     : GlobalMart Enterprise Lakehouse
Module      : Base Generator
Author      : Ambuj Kumar
Description : Base class for all enterprise data generators.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd

from .common import CommonUtils
from .config import config
from .logger import get_logger


class BaseGenerator(ABC):
    """
    Base class for all data generators.
    """

    def __init__(self, dataset_name: str):

        self.dataset_name = dataset_name

        self.logger = get_logger(dataset_name)

        self.output_path = (
            Path(
                config.get(
                    "output.base_path"
                )
            )
            / dataset_name
        )

        self.batch_id = CommonUtils.generate_batch_id()

    @abstractmethod
    def generate(self) -> pd.DataFrame:
        """
        Generate dataset.

        Must be implemented by child classes.
        """
        pass

    def validate(
        self,
        df: pd.DataFrame,
    ) -> None:
        """
        Validate generated dataframe.
        """

        CommonUtils.validate_dataframe(df)

        if df.duplicated().any():
            self.logger.warning(
                "Duplicate records detected."
            )

        self.logger.info(
            "Validation completed successfully."
        )

    def save(
        self,
        df: pd.DataFrame,
    ) -> None:
        """
        Save dataframe into supported formats.
        """

        CommonUtils.save_csv(
            df=df,
            output_path=self.output_path,
            file_name=self.dataset_name,
        )

        CommonUtils.save_parquet(
            df=df,
            output_path=self.output_path,
            file_name=self.dataset_name,
        )

    def run(self) -> pd.DataFrame:
        """
        Execute complete generator lifecycle.
        """

        self.logger.info(
            "Started %s generation.",
            self.dataset_name,
        )

        df = self.generate()

        self.validate(df)

        self.save(df)

        self.logger.info(
            "%s generation completed.",
            self.dataset_name,
        )

        return df