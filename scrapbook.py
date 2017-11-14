import Frame
import DiceRoll

f1 = Frame.Frame()
g1 = f1.createGame('GameOne')
f1.setGame(g1)

print(str(f1.getGame().getCurrentGameUID()) + ' # ' + str(f1.getGame().getGameCount()) + ' # ' + str(f1.getGame().getName()))
f1.reset()
print(str(f1.getGame().getCurrentGameUID()) + ' # ' + str(f1.getGame().getGameCount()) + ' # ' + str(f1.getGame().getName()))
f1.getGame().setName('GameTwo')
print(str(f1.getGame().getCurrentGameUID()) + ' # ' + str(f1.getGame().getGameCount()) + ' # ' + str(f1.getGame().getName()))

print(Frame.DiceRoll.rollInitiative(4))