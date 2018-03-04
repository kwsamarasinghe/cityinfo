import unittest

from engine.dataagents.exchange_rate_agent import ExchangeRateAgent
from engine.dataagents.weather_agent import WeatherAgent
from engine.dataagents.news_agent import NEWSAgent

class TestDataAgents(unittest.TestCase):

    exchangeRateAPIURL = "https://api.fixer.io/latest?base=GBP"

    weatherAPIURL = "http://api.apixu.com/v1/current.json?key=a94441e907c44144a6002524180403&q=London"

    newsAPIURL = "https://newsapi.org/v2/top-headlines?q=london&apiKey=90d620d913f74e1b8d8bf7d4a5426ad6"

    def test_exchangeagent_construction(self):
        exchangeRateAgent = ExchangeRateAgent(TestDataAgents.exchangeRateAPIURL)

    def test_exchangeagent_fetchdata(self):
        exchangeRateAgent = ExchangeRateAgent(TestDataAgents.exchangeRateAPIURL)
        response = exchangeRateAgent.fetchData()
        self.assertEqual(response, 200)

    def test_weather_construction(self):
        self.weatherAgent = WeatherAgent(TestDataAgents.weatherAPIURL)

    def test_weatheragent_fetchdata(self):
        weatherAgent = WeatherAgent(TestDataAgents.weatherAPIURL)
        response = weatherAgent.fetchData()
        self.assertEqual(response, 200)

    def test_newsagent_construction(self):
        newsAgent = NEWSAgent(TestDataAgents.newsAPIURL)

    def test_newsagent_fetchdata(self):
        newsAgent = NEWSAgent(TestDataAgents.newsAPIURL)
        response = newsAgent.fetchData()
        self.assertEqual(response, 200)
