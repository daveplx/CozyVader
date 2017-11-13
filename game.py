class Game:

    gameUID = 0

    def __init__(self, name, entityList=[], encounterList=[]):
        self.name = name
        self.entityList = entityList
        self.encounterList = encounterList
        self.gameUID = Game.gameUID; Game.gameUID += 1
        return


    @classmethod
    def getGameCount(cls):
        return Game.gameUID

    def getcurrentGame(self):
        return self.gameUID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        return

    def getEntityList(self):
        return self.entityList

    def setEntityList(self, entityList):
        self.entityList = entityList
        return

    def getEncounterList(self):
        return self.encounterList

    def setEncounterList(self, encounterList):
        self.encounterList = encounterList
        return

    def addEntity(self, entity):
        self.entityList.append(entity)
        return

    def removeEntity(self, entity):
        self.entityList.remove(entity)
        return

    def addEncounter(self, encounter):
        self.encounterList.append(encounter)
        return

    def removeEncounter(self, encounter):
        self.encounterList.remove(encounter)
        return

    def clearEntityList(self):
        self.entityList.clear()
        return

    def clearEncounterList(self):
        self.encounterList.clear()
        return
