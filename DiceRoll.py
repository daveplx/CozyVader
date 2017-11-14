import dice

def rollInitiative(dexterity_bonus):
    #returns a tuple of total roll, roll and bonus
    roll = dice.roll('1d20')
    return (roll[0] + dexterity_bonus, roll, dexterity_bonus)
