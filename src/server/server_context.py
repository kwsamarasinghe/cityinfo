import xml.etree.ElementTree as XMLParser

class ServerContext:

    def __init__(self, configFile):
        #Reads from config file
        print "Loading config file at "+configFile
        configXML = XMLParser.parse(configFile)
        root = configXML.getroot()

        #Reads server port
        self._serverParameters = {}
        serverPort = root.find('server').attrib['port']
        self._serverParameters['port'] = serverPort

        #Reads agent properties
        self._dataAgents = []
        propertyXML = root.find('dataagents')
        for agent in propertyXML:
            dataAgent = {}

            name = agent.attrib['name']
            dataAgent['name'] = name

            url = agent.attrib['url']
            dataAgent['url'] = url

            parameters = []
            for parameter in agent:
                _parameter = {}
                name = parameter.attrib['name']
                _parameter['name'] = name
                value = parameter.attrib['value']
                _parameter['value'] = value
                parameters.append(_parameter)

            dataAgent['parameters'] = parameters
            self._dataAgents.append(dataAgent)

    @property
    def serverParameters(self):
        return self._serverParameters

    @property
    def dataAgents(self):
        return self._dataAgents
