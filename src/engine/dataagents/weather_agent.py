from abc import ABCMeta
from urlparse import urlparse
import httplib
import json

from engine.data_agent import DataAgent
from engine.agent_response import AgentResponse

'''
Weather API agent which fetches the data from the the service
'''
class WeatherAgent:

    def __init__(self, url):
        self.url = url
        self.parsedURL = urlparse(url)
        self.connection = httplib.HTTPConnection(self.parsedURL.netloc)

    def fetchData(self):
        self.connection.request("GET", self.parsedURL.path+'?'+self.parsedURL.query)
        response = self.connection.getresponse()
        if(response.status == 200):
            responseData =json.loads(response.read())
            cityName = responseData['location']['name']
            date = responseData['location']['localtime']
            metrics = responseData['current']

            weatherData = {}
            weatherData['city'] = cityName
            weatherData['date'] = date
            weatherData['metrics'] = metrics
            agentResponse = AgentResponse('weather', self.url, weatherData)
            return agentResponse
        else:
            return None

DataAgent.register(WeatherAgent)
