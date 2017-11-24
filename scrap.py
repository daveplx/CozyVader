import dice


class Modifier():

    def __init__(self, modifier=0):
        self.modifier = modifier

    def getModifier(self):
        return self.modifier

    def setModifier(self, newModifier):
        try:
            if (-10 < int(newModifier) < 31):
                self.modifier = int(newModifier)
            else:
                raise OverflowError("Parameter out of bounds (-10 < p < 31)")
        except ValueError:
            raise ValueError("Invalid parameter given (must be int)")

