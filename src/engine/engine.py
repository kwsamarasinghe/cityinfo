from multiprocessing import Pool

from dataagents.exchange_rate_agent import ExchangeRateAgent
from dataagents.weather_agent import WeatherAgent
from dataagents.news_agent import NEWSAgent

#This class is the main component, which calls the relevant services and composes the info
class Engine:

    def __init__(self, dataAgentProperties):
        #Loads the data agents
        self.dataAgents = []
        for properties in dataAgentProperties:
            name = properties['name']
            url = properties['url']
            parameters = properties['parameters']

            #Append the query paramters
            p_first = True
            for parameter in parameters:
                p_name = parameter['name']
                p_value = parameter['value']
                if(p_first):
                    url = url+'?'+ p_name+'='+p_value
                    p_first = False
                else:
                    url = url+'&'+p_name+'='+p_value

            agent = self.loadAgent(name, url)
            self.dataAgents.append(agent)

    def loadAgent(self, name, url):
        if(name == 'exchangeRateAgent'):
            agent = ExchangeRateAgent(url)
        elif(name == 'newsAgent'):
            agent = NEWSAgent(url)
        elif(name == 'weatherAgent'):
            agent = WeatherAgent(url)
        else:
            raise Exception("Unknow agent")

        return agent

    #Returns the info
    def getInfo(self):
        #Exectues the data agent synchronously
        #TODO: implement asynchronous execution
        infoResponse = []
        for agent in self.dataAgents:
            agentResponse = agent.fetchData()
            infoResponse.append(agentResponse)
        return infoResponse

    #returns the updates
    def getInfoUpdate(self):
        return None
