import sys, traceback

from engine.engine import Engine
from server_context import ServerContext
from api.cityinfo_service import CityInfoService

#CityInfo RESTFull service
class Server:

    def __init__(self, configFile):
        try:
            self.engine = None

            #Builds the server context
            self.serverContext = ServerContext(configFile)
            #Data agents
            self._dataAgentsProperties =  self.serverContext.dataAgents
            #port
            self._serverPort = self.serverContext.serverParameters['port']

            #Intializes and starts the API
            cityinfoService = CityInfoService(self)
            cityinfoService.start()
            print "CityInfo service started at "+self._serverPort

        except Exception as exception:
            traceback.print_exc(file=sys.stdout)

    @property
    def serverPort(self):
        return self._serverPort

    @property
    def cityName(self):
        return self.serverContext.cityName

    def getEngine(self):
        self.engine = Engine(self._dataAgentsProperties)
        return self.engine


if __name__ == '__main__':
    from sys import argv
    server = Server(argv[1])
    #engine = Engine()
