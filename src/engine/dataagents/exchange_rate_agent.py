from abc import ABCMeta
from urlparse import urlparse
import httplib
import json

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
        url = self.parsedURL.path+'?'+self.parsedURL.query
        self.connection.request("GET", url)
        response = self.connection.getresponse()
        if(response.status == 200):
            #Only reads few currencies, for the moment USD, CHF, EUR
            responseData =json.loads(response.read())
            date = responseData['date']
            eur = responseData['rates']['EUR']
            usd = responseData['rates']['USD']
            chf = responseData['rates']['CHF']

            forexData = {}
            forexData['date'] = date
            forexData['currencies'] = {'EUR':eur, 'USD':usd,'CHF':chf}
            agentResponse = AgentResponse('forex', self.url, forexData)
            return agentResponse
        else:
            return None

DataAgent.register(ExchangeRateAgent)
