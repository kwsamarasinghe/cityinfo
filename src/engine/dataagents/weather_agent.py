from abc import ABCMeta
from urlparse import urlparse
import httplib

from engine.data_agent import DataAgent

'''
Weather API agent which fetches the data from the the service
'''
class WeatherAgent:

    def __init__(self, url):
        self.parsedURL = urlparse(url)
        self.connection = httplib.HTTPConnection(self.parsedURL.netloc)

    def fetchData(self):
        self.connection.request("GET", self.parsedURL.path+'?'+self.parsedURL.query)
        response = self.connection.getresponse()
        print response.read()
        return response.status

DataAgent.register(WeatherAgent)
