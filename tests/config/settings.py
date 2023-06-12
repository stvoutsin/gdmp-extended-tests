from tests.utils.decorator import Decorator
import yaml
import os


class Settings:
    """
    Attributes:
        ZEPPELIN_URL: str
        DOMAIN: object
    """

    ZEPPELIN_URL: str
    DOMAIN: object

    def __init__(self):
        self.load_settings("../../settings.yml")

    def load_settings(self, settings_file: str):
        """
        Load the Settings from the "s
        Returns:

        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        settings_file_path = os.path.join(current_dir, "../..", "settings.yml")
        with open(settings_file_path) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        self.DOMAIN = config["DOMAIN"]
        self.ZEPPELIN_URL = Decorator.decorate_https(self.DOMAIN)


settings = Settings()
