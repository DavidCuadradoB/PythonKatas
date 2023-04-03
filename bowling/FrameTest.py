import unittest

from bowling.Frame import Frame


class MyTestCase(unittest.TestCase):
    frame = Frame()

    def test_get_score_givenFirstAndSecondStrikeEquals_shouldSumOfBoth(self):
        firstStrike = 10
        secondStrike = 4
        self.frame.save_first_strike(firstStrike)
        self.frame.save_second_strike(secondStrike)

        score = self.frame.get_score()
        self.assertEqual(score, firstStrike + secondStrike)  # add assertion here

    def test_isSpare_givenSumOfFirstAndSecondStrikeEquals10_shouldReturnTrue(self):
        firstStrike = 7
        secondStrike = 3
        self.frame.save_first_strike(firstStrike)
        self.frame.save_second_strike(secondStrike)

        isSpare = self.frame.is_spare()
        self.assertEqual(isSpare, True)

    def test_isSpare_givenSumOfFirstAndSecondStrikeIsLessThan10_shouldReturnFalse(self):
        firstStrike = 1
        secondStrike = 1
        self.frame.save_first_strike(firstStrike)
        self.frame.save_second_strike(secondStrike)

        isSpare = self.frame.is_spare()
        self.assertEqual(isSpare, False)


if __name__ == '__main__':
    unittest.main()
