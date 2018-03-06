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
        self.currencies = ['EUR', 'CHF', 'USD', 'GBP']

    def fetchData(self):
        #try:
            url = self.parsedURL.path+'?'+self.parsedURL.query
            self.connection.request("GET", url)
            response = self.connection.getresponse()
            if(response.status == 200):
                #Only reads few currencies, for the moment USD, CHF, EUR
                responseData =json.loads(response.read())
                date = responseData['date']

                #Retrives the currencies
                baseCurrency = self.parsedURL.query.split('=')[1]
                exchangeRates = {}
                for currency in self.currencies:
                    if currency != baseCurrency:
                        exchangeRates[currency] = responseData['rates'][currency]

                print exchangeRates

                forexData = {}
                forexData['date'] = date
                forexData['currencies'] = exchangeRates
                agentResponse = AgentResponse('forex', self.url, forexData)
                return agentResponse
            else:
                return None
        #except Exception as e:
        #    print "Error retrieving data from  "+self.parsedURL.netloc + self.parsedURL.path
        #    return None

DataAgent.register(ExchangeRateAgent)
