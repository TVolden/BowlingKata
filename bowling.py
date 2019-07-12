class BowlingGame:

    def __init__(self):
        self._rolls = [0 for i in range(21)]
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1

    def score(self):
        score = 0
        i = 0
        for frame in range(10):
            if self._rolls[i] + self._rolls[i + 1] == 10:
               score += 10 + self._rolls[i + 2]
               i += 2
            else:
                score += self._rolls[i] + self._rolls[i + 1]
                i += 2
        return score
