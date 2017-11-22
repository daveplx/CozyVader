import scrap
import unittest
import random


class TestDiceRolls(unittest.TestCase):
    def test_rollDice(self):
        randint_a = random.randint(1, 10)
        randint_b = random.randint(1, 10)
        diceResult = scrap.rollDice(randint_a, randint_b)
        self.assertLessEqual(sum(diceResult), (randint_a * randint_b))
        self.assertGreaterEqual(sum(diceResult), randint_a)
        resultBoolean = True
        for roll in diceResult:
            if roll < 1 or roll > randint_b:
                resultBoolean = False
        self.assertTrue(resultBoolean)

    def test_setNumOfDice(self):
        randint_a = random.randint(0, 16)
        scrap.setNumOfDice(randint_a)
        self.assertEqual(randint_a, scrap.numOfDice)

    def test_setNumOfDiceNonInteger(self):
        with self.assertRaises(ValueError):
            scrap.setNumOfDice('a')

    def test_setNumOfSides(self):
        randint_a = random.randint(0, 16)
        scrap.setNumOfSides(randint_a)
        self.assertEqual(randint_a, scrap.numOfSides)

    def test_setNumOfSidesNonInteger(self):
        with self.assertRaises(ValueError):
            scrap.setNumOfSides('s')

    def test_setStat(self):
        randint_a = random.randint(-4, 7)
        scrap.setStatModifier('str', randint_a)
        self.assertEqual(randint_a, scrap.statModifiers['str'])

    def test_setStatNonInteger(self):
        with self.assertRaises(ValueError):
            scrap.setStatModifier('int', 'b')

    def test_setNonExistentStat(self):
        with self.assertRaises(ValueError):
            scrap.setStatModifier('a', 3)

    def test_setStatOutOfRange(self):
        with self.assertRaises(OverflowError):
            scrap.setStatModifier('wis', 8)

    def test_setCurrentStatModifierByStat(self):
        scrap.setCurrentStatModifierByStat('int')
        self.assertEqual(scrap.statModifiers['int'], scrap.currentStatModifier)

    def test_setCurrentStatModifierByNonExistentStat(self):
        with self.assertRaises(ValueError):
            scrap.setCurrentStatModifierByStat(4)
            scrap.setCurrentStatModifierByStat('bla')

    def test_toggleCurrentStatModifierIsOn(self):
        beforeToggle = scrap.currentStatModifierIsOn
        scrap.toggleCurrentStatModifierIsOn()
        self.assertFalse(beforeToggle == scrap.currentStatModifierIsOn)

    def test_toggleProficiencyBonusIsOn(self):
        beforeToggle = scrap.proficiencyBonusIsOn
        scrap.toggleProficiencyBonusIsOn()
        self.assertFalse(beforeToggle == scrap.proficiencyBonusIsOn)


if __name__ == '__main__':
    unittest.main()
