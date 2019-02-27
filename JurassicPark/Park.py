from Dinosaur import *
from Zone import *

class Park:

    zoneList=[]

    def __init__(self,name):
        self.name = name
        self.zoneList = []

    def __str__(self):
        return self.name + '\n' + '\n'.join(str(zone) for zone in self.zoneList)
    

    def loadZones(self,fileName):
        file = open(fileName,"r")
        inputLines = file.read().splitlines()
        for line in inputLines:
            tokens = line.split(",")
            self.addZone(Zone(tokens[0],tokens[1],tokens[2]))
        file.close()
    
    def loadDinosaurs(self,fileName):
        file = open(fileName,"r")
        inputLines = file.read().splitlines()
        i = 0
        for line in inputLines:
            tokens = line.split(",")
            dino = Dinosaur (tokens[0],tokens[1],tokens[2],tokens[3])
            for i in range(len(self.zoneList)):
                if self.zoneList[i].getZoneCode() == dino.getZoneCode():
                    self.zoneList[i].addToDinosaurList(dino)
                i+=1


    #-----------------Gettes and Setters-----------------#
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name

    def addZone(self,zone):
        self.zoneList.append(zone)

    def getZoneList(self):
        return self.zoneList