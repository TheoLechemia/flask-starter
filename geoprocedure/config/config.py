from pathlib import Path

import toml

from geoprocedure.config.config_schema import ConfigSchema

from geoprocedure.env import APP_DIR


def load_config():
    config_toml = toml.load(str(APP_DIR / "config" / "config.toml"))
    config = ConfigSchema().load(config_toml)
    return config


config = load_config()
