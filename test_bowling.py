import unittest
import bowling as bowl

class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = bowl.BowlingGame()

    def test_roll_all_gutter(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def roll_many(self, rolls, pins):
        for roll in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()
