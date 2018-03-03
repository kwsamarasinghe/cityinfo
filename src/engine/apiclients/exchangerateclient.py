from abc import ABCMeta

from engine.apiclient import APIClient

'''
Exchange rate client fetches the data from the the service
'''
class ExchangeRateClient:

    def __init__(self, url):
        self.url = url

    def extractData():
        print "extracting data"
