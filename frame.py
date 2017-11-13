import game
import player
import npc
import encounter

Game = game.Game
Player = player.Player
NPC = npc.NPC
Encounter = encounter.Encounter


class Frame:

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

