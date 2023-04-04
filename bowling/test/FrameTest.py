import unittest

from bowling.Frame import Frame


class MyTestCase(unittest.TestCase):
    frame = Frame()

    def test_get_score_given_first_and_second_try_equals_should_be_sum_of_both(self):
        first_strike = 10
        second_strike = 4
        self.frame.save_first_try(first_strike)
        self.frame.save_second_try(second_strike)

        score = self.frame.get_score()
        self.assertEqual(score, first_strike + second_strike)  # add assertion here

    def test_is_spare_given_sum_of_first_and_second_try_equals_10_should_return_true(self):
        first_strike = 7
        second_strike = 3
        self.frame.save_first_try(first_strike)
        self.frame.save_second_try(second_strike)

        is_spare = self.frame.is_spare()
        self.assertEqual(is_spare, True)

    def test_is_spare_givenSumOfFirstAndSecondTryIsLessThan10_shouldReturnFalse(self):
        first_strike = 1
        second_strike = 1
        self.frame.save_first_try(first_strike)
        self.frame.save_second_try(second_strike)

        is_spare = self.frame.is_spare()
        self.assertEqual(is_spare, False)

    def test_is_stike_given_first_try_equals_10_should_return_true(self):
        self.frame.save_first_try(10)
        is_strike = self.frame.is_strike()
        self.assertEqual(is_strike, True)

    def test_is_stike_given_first_try_less_than_10_should_return_false(self):
        self.frame.save_first_try(1)
        is_strike = self.frame.is_strike()
        self.assertEqual(is_strike, False)


if __name__ == '__main__':
    unittest.main()
