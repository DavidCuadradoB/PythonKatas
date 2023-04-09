import unittest

from bowling.Game import Game


class GameTest(unittest.TestCase):
    def test__throw__given_game_with_frame_full__should_create_new_frame(self):
        self.game = Game()
        self.game.throw(1)
        self.game.throw(2)
        self.game.throw(10)
        self.game.throw(4)
        self.game.throw(5)
        number_of_frames = self.game.get_turn()
        self.assertEqual(number_of_frames, 3)  # add assertion here


if __name__ == '__main__':
    unittest.main()
