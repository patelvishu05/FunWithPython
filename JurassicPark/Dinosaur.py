class Dinosaur:

    def __init__(self,name,dinoType,diet,zoneCode):
        self.name = name
        self.dinoType = dinoType
        self.diet = diet
        self.zoneCode = zoneCode

    def __str__(self):
        return " * " + self.name + " - " + self.dinoType + " (" + self.parseDiet() +")"

    #----------Getters and Setters----------------#

    def parseDiet(self):
        return "not carnivore" if self.diet == 'true' else "carnivore"

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getDinoType(self):
        return self.dinoType
    
    def setDinoType(self,dinoType):
        self.dinoType = dinoType
    
    def getDiet(self):
        return self.diet

    def setDiet(self,diet):
        self.diet = diet
    
    def getZoneCode(self):
        return self.zoneCode

    def setZoneCode(self,zoneCode):
        self.zoneCode = zoneCode
