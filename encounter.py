class Encounter:

    encounterUID = 0

    def __init__(self, name, players=[]):
        self.name = name
        self.players = players
        self.encounterUID = Encounter.encounterUID; Encounter.encounterUID += 1
        return

