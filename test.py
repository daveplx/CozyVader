import dicier
import scrap
import unittest
import random


class TestScrap(unittest.TestCase):

    def test_getModifier(self):
        session1 = scrap.Modifier(2)
        self.assertEqual(session1.getModifier(), 2)

    def test_setModifier(self):
        session1 = scrap.Modifier()
        newModifier = 1
        session1.setModifier(newModifier)
        self.assertEqual(newModifier, session1.getModifier())

    def test_setModifierNegative(self):
        session1 = scrap.Modifier()
        newModifier = -1
        session1.setModifier(newModifier)
        self.assertEqual(newModifier, session1.getModifier())

    def test_setModifierString(self):
        session1 = scrap.Modifier()
        newModifier = 'a'
        with self.assertRaises(ValueError):
            session1.setModifier(newModifier)

    def test_setModifierOutOfBounds(self):
        session1 = scrap.Modifier()
        newModifier = random.randint(-999, -10)
        with self.assertRaises(OverflowError):
            session1.setModifier(newModifier)
        newModifier = random.randint(31, 999)
        with self.assertRaises(OverflowError):
            session1.setModifier(newModifier)

    def test_dicierRoll(self):
        dice = random.randint(1,50)
        sides = random.randint(1, 20)
        rollString = str(dice) + 'd' + str(sides)
        roll = dicier.roll(rollString)
        totalRoll = sum(roll)
        self.assertEqual(dice, len(roll))
        for die in roll:
            self.assertGreaterEqual(die, 1)
            self.assertLessEqual(die, sides)
        self.assertGreaterEqual(totalRoll, dice)
        self.assertLessEqual(totalRoll, dice * sides)

    def test_dicierRollNoD(self):
        dice = random.randint(1, 50)
        sides = random.randint(1, 20)
        rollString = str(dice) + 't' + str(sides)
        with self.assertRaises(SyntaxError):
            dicier.roll(rollString)

    def test_dicierRollNoDice(self):
        dice = ''
        sides = random.randint(1, 20)
        rollString = str(dice) + 'd' + str(sides)
        roll = dicier.roll(rollString)
        totalRoll = sum(roll)
        self.assertEqual(1, len(roll))
        self.assertGreaterEqual(totalRoll, 1)
        self.assertLessEqual(totalRoll, sides)

    def test_dicierRollNoSides(self):
        dice = random.randint(1, 50)
        sides = ''
        rollString = str(dice) + 'd' + str(sides)
        with self.assertRaises(ValueError):
            dicier.roll(rollString)

if __name__ == '__main__':
    unittest.main()
