import unittest
import sys
sys.path.append('../../')
from engine.apiclients.exchangerateclient import ExchangeRateClient

class TestAPIClients(unittest.TestCase):

    def test_exchangeclient_construction(self):
        exchangeRateAPIURL = 'https://api.fixer.io/latest?base=USD'
        ExchangeRateClient(exchangeRateAPIURL)
