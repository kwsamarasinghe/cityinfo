'''
AgentResponse class represents the response from each agent
'''

class AgentResponse:

    def __init__(self, type, source, data):
        self._type = type
        self._source = source
        self._data = data

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, typeValue):
        self._type = typeValue

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, sourceValue):
        self._source = sourceValue

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, sourceValue):
        self._data = dataValue
