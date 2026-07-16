"""
Project     : GlobalMart Enterprise Lakehouse
Module      : Configuration Manager
Author      : Ambuj Kumar
Description : Handles application configuration loading and validation.
"""

import yaml
from pathlib import Path
from typing inport Any

class ConfigManager:
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> dict:
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )
        
        with self.config_path.open("r") as file:
            return yaml.safe_load(file)
        
    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split(".")
        value = self.config

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        
        return value
    
CONFIG_PATH = (
    Path(__file__).resolve().parents[2]
    / "configs"
    / "config.yml"
)

config = ConfigManager(CONFIG_PATH)

