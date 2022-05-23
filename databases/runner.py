from pathlib import Path
from configparser import ConfigParser
from sqlalchemy import engine_from_config
from sqlalchemy.orm import Session

class Engine:
    def _get_config(self, config_file_name: str, engine_type: str) -> dict:
        config = ConfigParser()
        config.read(Path(Path(__file__).parent, config_file_name).resolve())
        return config._sections[engine_type]

    def __init__(self, engine_type: str, config_file_name: str = "config.ini", config_prefix: str = "db."):
        self.config = self._get_config(config_file_name=config_file_name, engine_type=engine_type)
        self.engine = engine_from_config(self.config, prefix=config_prefix)
