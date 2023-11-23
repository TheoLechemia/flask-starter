from pathlib import Path

import toml

from .config_schema import ConfigSchema

from env import APP_DIR


def load_config():
    config_toml = toml.load(str(APP_DIR / "config" / "config.toml"))
    config = ConfigSchema().load(config_toml)
    return config


config = load_config()
