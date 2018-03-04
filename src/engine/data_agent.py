from abc import *

'''
    Abstract data provider
'''
class DataAgent:

    __metaclass__ = ABCMeta

    @abstractproperty
    def url(self):
        print ""

    @abstractmethod
    def extractData():
        return

    @classmethod
    def getURL():
        return self.url
