import unittest

from bowling.Game import GameIsOver
import bowling.Game as GameClass


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = GameClass.Game()

    def test__throw__given_game_with_frame_full__should_create_new_frame(self):
        self.game.throw(1)
        self.game.throw(2)
        self.game.throw(10)
        self.game.throw(4)
        self.game.throw(5)
        number_of_frames = self.game.get_turn()
        self.assertEqual(number_of_frames, 3)  # add assertion here

    def test_throw__given_a_full_game__should_throw_an_exception(self):
        self.game.throw(10)
        self.game.throw(10)
        self.game.throw(10)
        self.game.throw(10)
        self.game.throw(10)
        self.game.throw(10)
        self.game.throw(10)
        self.game.throw(10)
        self.game.throw(10)
        self.game.throw(10)

        with self.assertRaises(GameIsOver) as context:
            self.game.throw(1)

        self.assertTrue('Game is Over' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
