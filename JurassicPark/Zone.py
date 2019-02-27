import copy
from Dinosaur import *

class Zone():

    dinosaurList=[]

    def __init__(self,zoneCode,rating):
        self.zoneCode = zoneCode
        self.rating = rating
        self.dinosaurList = []

    def __str__(self):
        return self.zoneCode + "\t" + self.rating

    #----------------Getters and Setters-------------------#

    def getZoneCode(self):
        return self.zoneCode
    
    def setZoneCode(self,zoneCode):
        self.zoneCode = zoneCode

    def getRating(self):
        return self.rating
    
    def setRating(self,rating):
        self.rating = rating
    
    def getDinosaurList(self):
        return self.dinosaurList
    
    def setDinosaurList(self,dinosaurList):
        self.dinosaurList = copy.deepcopy(dinosaurList)
    
    def addToDinosaurList(self,dino):
        self.dinosaurList.append(dino)

