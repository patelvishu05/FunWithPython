from Dinosaur import *
from Zone import *

class Park:

    zoneList=[]

    def __init__(self,name):
        self.name = name
        self.zoneList = []

    def __str__(self):
        return "Welcome to " + self.name + '!\n' + "----------------------------\n" + '\n'.join(str(zone) for zone in self.zoneList)
    
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

    def relocate(self,name,zoneCode):
        i=0
        j=0
        dino = None
        for i in range(len(self.zoneList)):
            for j in range(len(self.zoneList[i].getDinosaurList())):
                if self.zoneList[i].getDinosaurList()[j].getName() == name:
                    dino = self.zoneList[i].getDinosaurList()[j]
                j+=1
            i+=1
        i=0
        dino.setZoneCode(zoneCode)
        for i in range(len(self.zoneList)):
            if self.zoneList[i].getZoneCode() == zoneCode:
                self.zoneList[i].addToDinosaurList(dino)
            
    def save(self,fileName):
        file = open(fileName,"w+")
        for zone in self.zoneList:
            for dino in zone.getDinosaurList():
                file.write(dino.getName() + "," + dino.getDinoType() + "," + dino.getDiet() + "," + dino.getZoneCode() + '\n')
        file.close()

    #-----------------Getters and Setters-----------------#
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name

    def addZone(self,zone):
        self.zoneList.append(zone)

    def getZoneList(self):
        return self.zoneList