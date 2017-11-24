from random import randint

def roll(rollString):
    try:
        if not str(rollString).__contains__('d'):
            raise SyntaxError("SyntaxError: String must contain 'd' (e.g. '3d6' or 'd20')")
        splitString= str(rollString).split('d')
        if splitString[0] == '':
            dice = 1
        else:
            dice = int(splitString[0])
        #print('dice: ', dice)
        sides = int(splitString[1])
        #print('sides: ', sides)
        rolls = []
        for x in range(0, dice):
            rolls.append(randint(1, sides))
        #print('rolls:\n', rolls)
        #print('len(rolls): ', len(rolls))
        return rolls
    except ValueError:
        raise ValueError("Invalid parameter given (must be 'xdy', where x=dice and y=sides, \
                        e.g. '3d6' or 'd20' instead of '1d20')")