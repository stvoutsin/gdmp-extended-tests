import unittest
import websocket
from tests.config.settings import settings
from tests.utils.decorator import Decorator


class WebSocketTest(unittest.TestCase):
    """
    Tests that a Websocket connection to the domain works as expected
    """

    def test_websocket_connection(self):
        """
        Test a WSS connection to the domain
        """
        url = Decorator.decorate_wss(settings.DOMAIN)
        # Connect to the WebSocket URL
        ws = websocket.WebSocket()
        ws.connect(url)

        # Check if the connection is open
        self.assertTrue(ws.connected)

        # Close the WebSocket connection
        ws.close()


if __name__ == "__main__":
    unittest.main()
