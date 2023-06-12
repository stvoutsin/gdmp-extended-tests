from tests.utils.decorator import Decorator
import yaml


class Settings:
    """
    Attributes:
        ZEPPELIN_URL: str
        DOMAIN: object
    """

    ZEPPELIN_URL: str
    DOMAIN: object

    def __init__(self):
        self.load_settings("../settings.yml")

    def load_settings(self, settings_file: str):
        """
        Load the Settings from the "s
        Returns:

        """
        with open(settings_file) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        self.DOMAIN = config["DOMAIN"]
        self.ZEPPELIN_URL = Decorator.decorate_https(self.DOMAIN)


settings = Settings()
