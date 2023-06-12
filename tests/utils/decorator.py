class Decorator:
    @staticmethod
    def decorate_http(string: str) -> str:
        """
        Decorate an HTTP URL given a domain URL as a string
        Args:
            string (str): String to decorate

        Returns:
            string: Decorated string
        """
        return f"http://{string}/"

    @staticmethod
    def decorate_https(string: str) -> str:
        """
        Decorate an HTTPS URL given a domain URL as a string
        Args:
            string (str): String to decorate

        Returns:
            string: Decorated string
        """
        return f"https://{string}/"

    @staticmethod
    def decorate_wss(string: str) -> str:
        """
        Decorate a WSS endpoint given a domain URL as a string
        Args:
            string (str): String to decorate

        Returns:
            string: Decorated string
        """
        return f"wss://{string}/ws"
