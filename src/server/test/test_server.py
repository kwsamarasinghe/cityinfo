import unittest
from server.server_context import ServerContext

class TestServer(unittest.TestCase):

    def test_servercontext_construction(self):
        serverContext = ServerContext('src/server/test/mockconf.xml')
