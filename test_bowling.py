import unittest
import bowling as bowl

class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = bowl.BowlingGame()

    def test_roll_all_gutter(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_roll_all_once(self):
        self.roll_many(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_roll_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.assertEqual(self.game.score(), 16)
    
    def test_roll_perfect_game(self):
        for x in range(12):
            self.game.roll(10)
        self.assertEqual(self.game.score(), 300)

    def roll_many(self, rolls, pins):
        for roll in range(rolls):
            self.game.roll(pins)
        
    def test_roll_perfect_score_is_300(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.score(), 300)

if __name__ == '__main__':
    unittest.main()
