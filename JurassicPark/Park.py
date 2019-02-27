from Dinosaur import *
from Zone import *

class Park:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def loadZones(self,fileName):
        file = open(fileName,"r")
        inputLines = file.read().splitlines()
        

    
    def loadDinosaurs(self,fileName):



    #-----------------Gettes and Setters-----------------#
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
    
