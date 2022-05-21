from configparser import ConfigParser

class Engine:
    def _get_config(self, config_file_name: str) -> dict:
			config = ConfigParser.ConfigParser().read(config_file_name)
			return config.__dict__

    def __init__(self, config_file_name: str = "config.ini", config_prefix: str = "bridge") -> None:
        self.config = self._get_config()

        self.engine = engine_from_config(self.config, prefix=config_prefix)
    