import sys
from pathlib import Path
from configparser import ConfigParser
from sqlalchemy import engine_from_config
from sqlalchemy.orm import Session

sys.path.insert(0, Path(__file__).parent.parent.as_posix())

from databases.common import transcation_isolation
from databases.bridge.bridge import BASE

class Engine:
    def _get_config(self, config_file_name: str) -> dict:
        print(config_file_name)
        config = ConfigParser()
        config.read(config_file_name)
        print(config.sections())
        print("hello world")
        return config.__dict__

    def __init__(self, config_file_name: str = "config.ini", config_prefix: str = "db") -> None:
        self.config = self._get_config(config_file_name=config_file_name)
        self.engine = engine_from_config(
            self.config,
            prefix=config_prefix,
        )

    @transcation_isolation
    def create_shipment_table(self, session: Session) -> None:
        BASE.metadata.create_all(self.engine)

e = Engine()
e.create_shipment_table()
