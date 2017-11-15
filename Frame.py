import Game
import Player
import Npc
import Encounter
import DiceRoll

Game = Game.Game
Player = Player.Player
NPC = Npc.Npc
Encounter = Encounter.Encounter


class Frame:

    @classmethod
    def createGame(cls, name='', entityList=[], encounterList=[]):
        return Game(name, entityList, encounterList)

    def __init__(self, game=None):
        self.game = game
        return

    def reset(self):
        self.game = Game()
        return

    def getGame(self):
        return self.game

    def setGame(self, game):
        self.game = game
        return

