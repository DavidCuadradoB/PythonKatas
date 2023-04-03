import unittest

from bowling.Frame import Frame


class MyTestCase(unittest.TestCase):
    frame = Frame()

    def test_get_score_givenFirstAndSecondTryEquals_shouldSumOfBoth(self):
        firstStrike = 10
        secondStrike = 4
        self.frame.save_first_try(firstStrike)
        self.frame.save_second_try(secondStrike)

        score = self.frame.get_score()
        self.assertEqual(score, firstStrike + secondStrike)  # add assertion here

    def test_is_spare_givenSumOfFirstAndSecondTryEquals10_shouldReturnTrue(self):
        firstStrike = 7
        secondStrike = 3
        self.frame.save_first_try(firstStrike)
        self.frame.save_second_try(secondStrike)

        isSpare = self.frame.is_spare()
        self.assertEqual(isSpare, True)

    def test_is_spare_givenSumOfFirstAndSecondTryIsLessThan10_shouldReturnFalse(self):
        firstStrike = 1
        secondStrike = 1
        self.frame.save_first_try(firstStrike)
        self.frame.save_second_try(secondStrike)

        isSpare = self.frame.is_spare()
        self.assertEqual(isSpare, False)

    def test_is_stike_givenFirstTryEquals10_shouldReturnTrue(self):
        self.frame.save_first_try(10)
        isStrike = self.frame.is_strike()
        self.assertEqual(isStrike, True)

    def test_is_stike_givenFirstTryLessThan10_shouldReturnFalse(self):
        self.frame.save_first_try(1)
        isStrike = self.frame.is_strike()
        self.assertEqual(isStrike, False)


if __name__ == '__main__':
    unittest.main()
