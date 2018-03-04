from abc import ABCMeta
from urlparse import urlparse
import httplib

from engine.data_agent import DataAgent
from engine.agent_response import AgentResponse

'''
Exchange rate client fetches the data from the the service
'''
class ExchangeRateAgent:

    def __init__(self, url):
        self.url = url
        self.parsedURL = urlparse(url)
        self.connection = httplib.HTTPConnection(self.parsedURL.netloc)

    def fetchData(self):
        self.connection.request("GET", self.parsedURL.path+'?'+self.parsedURL.query)
        response = self.connection.getresponse()
        if(response.status == 200):
            agentResponse = AgentResponse('forex', self.url, response.read())
            return response.status
        else:
            return None

DataAgent.register(ExchangeRateAgent)
