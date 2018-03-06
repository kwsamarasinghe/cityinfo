from abc import ABCMeta
from urlparse import urlparse
import httplib
import json

from engine.data_agent import DataAgent
from engine.agent_response import AgentResponse

'''
NEWS API agent which fetches the data from newsapi.org API
'''
class NEWSAgent:

    def __init__(self, url):
        self.url = url
        self.parsedURL = urlparse(url)
        self.connection = httplib.HTTPConnection(self.parsedURL.netloc)

    def fetchData(self):
        try:
            url = self.parsedURL.path+'?'+self.parsedURL.query
            self.connection.request("GET", url)
            response = self.connection.getresponse()
            if(response.status == 200):
                responseData = json.loads(response.read())
                status = responseData['status']
                if(status == 'ok'):
                    articles = responseData['articles']
                    newsArticles = []
                    for article in articles:
                        newsArticle = {}
                        newsArticle['name']=article['source']['name']
                        newsArticle['title']=article['title']
                        newsArticle['articleURL']=article['url']
                        newsArticles.append(newsArticle)

                    agentResponse = AgentResponse('news', self.url, newsArticles)
                    print agentResponse
                    return agentResponse
                else:
                    return None
            else:
                return None
        except Exception as e:
            print "Error retrieving data from  "+self.parsedURL.netloc + self.parsedURL.path
            return None

DataAgent.register(NEWSAgent)
