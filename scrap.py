import dice

numOfDice = 0
numOfSides = 0
statModifiers = {
    'str': 0,
    'con': 0,
    'dex': 0,
    'int': 0,
    'wis': 0,
    'cha': 0
}
currentStatModifier = 0
currentStatModifierIsOn = False
proficiencyBonus = 0
proficiencyBonusIsOn = False


def rollDice(numOfDice, numOfSides):
    diceRoll = dice.roll(str(numOfDice) + 'd' + str(numOfSides))
    return diceRoll


def setNumOfDice(newNumberOfDice):
    global numOfDice
    try:
        numOfDice = int(newNumberOfDice)
    except ValueError:
        raise ValueError('Wrong parameter value (must be integer)')


def setNumOfSides(newNumberOfSides):
    global numOfSides
    try:
        numOfSides = int(newNumberOfSides)
    except ValueError:
        raise ValueError('Wrong parameter value (must be integer)')


def statIsInvalid(stat):
    global statModifiers
    if stat not in statModifiers:
        raise ValueError("%s is not a valid stat ('str', 'con', ...)", stat)


def setStatModifier(stat, modifier):
    global statModifiers
    if not statIsInvalid(stat):
        try:
            if int(modifier) not in range(-4, 8):
                raise OverflowError("%d is out of range (-4 .. 7)", modifier)
            statModifiers[stat] = int(modifier)
        except ValueError:
            raise ValueError('Wrong parameter value (must be integer)')


def setCurrentStatModifierByStat(stat):
    global currentStatModifier
    global statModifiers
    if not statIsInvalid(stat):
        currentStatModifier = statModifiers[stat]


def toggleCurrentStatModifierIsOn():
    global currentStatModifierIsOn
    currentStatModifierIsOn = not currentStatModifierIsOn


def toggleProficiencyBonusIsOn():
    global proficiencyBonusIsOn
    proficiencyBonusIsOn = not proficiencyBonusIsOn
