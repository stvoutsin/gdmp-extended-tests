def empty_str_validator(f):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise ValueError("Can't decorate empty string")
            if not arg.strip():
                raise ValueError("Can't decorate empty string")
        return f(*args)

    return wrapper


class Decorator:
    @staticmethod
    @empty_str_validator
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
    @empty_str_validator
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
    @empty_str_validator
    def decorate_wss(string: str) -> str:
        """
        Decorate a WSS endpoint given a domain URL as a string
        Args:
            string (str): String to decorate

        Returns:
            string: Decorated string
        """
        return f"wss://{string}/ws"
