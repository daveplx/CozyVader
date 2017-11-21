import dice

diceSides = 6

diceCount = 3

stats = {'dex' : 3, 'str' : 0 }

modifier = stats['dex']

modifierIsOn = True

proficiency = 2

proficiencyIsOn = False


def rollDice(diceCount, diceSides, TotalModifier):
    callParameter = str(diceCount) + 'd' + str(diceSides)
    print(dice.roll(callParameter))


def setDiceSides(numberOfSides):
    global diceSides
    diceSides = numberOfSides

def setDiceCount(numberOfDice):
    global diceCount
    diceCount= numberOfDice

def setModifier(stat):
    global stats
    global modifier
    modifier = stats[stat]

def setStat(stat, modifier):
    global stats
    stats[stat] = modifier

def setProficiency(proficiencyValue):
    global proficiency
    proficiency = proficiencyValue

def toggleProficiency():
    global proficiencyIsOn
    proficiencyIsOn = not proficiencyIsOn

def toggleModifier():
    global modifierIsOn
    modifierIsOn = not modifierIsOn

###

rollDice(diceCount, diceSides, modifier)

setDiceCount(4)
setDiceSides(8)

rollDice(diceCount, diceSides, modifier)

print(modifier)
setModifier('str')
print(modifier)

setStat('str', 2)
setModifier('str')
print(modifier)
