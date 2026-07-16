"""
Project     : GlobalMart Enterprise Lakehouse
Module      : Configuration Manager
Author      : Ambuj Kumar
Description : Handles application configuration loading and validation.
"""

from pathlib import Path
from typing import Any

import yaml

# ==========================================================
# Constants
# ==========================================================

CONFIG_DIRECTORY = "configs"
CONFIG_FILE_NAME = "generator.yml"

REQUIRED_KEYS = [
    "environment",
    "generation",
    "datasets",
    "output",
]


# ==========================================================
# Configuration Manager
# ==========================================================

class ConfigManager:
    """
    Loads and provides access to the application configuration.

    Configuration is loaded from a YAML file and supports
    nested key access using dot notation.

    Example
    -------
    >>> config.get("datasets.customers.records")
    >>> config.get("output.base_path")
    """

    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> dict[str, Any]:
        """
        Load configuration from YAML file.

        Returns
        -------
        dict[str, Any]
            Parsed configuration dictionary.

        Raises
        ------
        FileNotFoundError
            If configuration file does not exist.

        ValueError
            If configuration file is empty or missing
            required sections.
        """

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        with self.config_path.open(
            mode="r",
            encoding="utf-8",
        ) as file:

            config = yaml.safe_load(file)

        if not config:
            raise ValueError(
                f"Configuration file '{self.config_path}' is empty."
            )

        self._validate(config)

        return config

    def _validate(
        self,
        config: dict[str, Any],
    ) -> None:
        """
        Validate required configuration sections.

        Parameters
        ----------
        config : dict[str, Any]
            Configuration dictionary.

        Raises
        ------
        ValueError
            If a required configuration section is missing.
        """

        for key in REQUIRED_KEYS:
            if key not in config:
                raise ValueError(
                    f"Missing required configuration section: '{key}'"
                )

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a configuration value using dot notation.

        Parameters
        ----------
        key : str
            Configuration key.

            Example:
            datasets.customers.records

        default : Any, optional
            Default value if key does not exist.

        Returns
        -------
        Any
            Configuration value.
        """

        value: Any = self.config

        for part in key.split("."):

            if not isinstance(value, dict):
                return default

            value = value.get(part)

            if value is None:
                return default

        return value


# ==========================================================
# Singleton Configuration Instance
# ==========================================================

CONFIG_PATH = (
    Path(__file__).resolve().parents[2]
    / CONFIG_DIRECTORY
    / CONFIG_FILE_NAME
)

config = ConfigManager(CONFIG_PATH)