from configparser import ConfigParser

from functools import wraps
from sqlalchemy import engine_from_config
from sqlalchemy.orm import Session
from models import Base


def transcation_isolation(func):
    @wraps(func)
    def func_wrapper(self, *args, **kwargs):
        with Session(self.engine) as session:
            return func(self, *args, **kwargs, session=session)

class Engine:
    def _get_config(self, config_file_name: str) -> dict:
        config = ConfigParser.ConfigParser().read(config_file_name)
        return config.__dict__

    def __init__(self, config_file_name: str = "config.ini", config_prefix: str = "db") -> None:
        self.config = self._get_config(config_file_name=config_file_name)
        self.engine = engine_from_config(
            self.config,
            prefix=config_prefix,
        )

    @transcation_isolation
    def create_tables(self, session: Session) -> None:
        Base.metadata.create_all(self.engine)
