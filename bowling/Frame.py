class Frame(object):
    firstStrike = 0
    secondStrike = 0

    def get_score(self):
        return self.firstStrike + self.secondStrike

    def save_first_strike(self, value):
        self.firstStrike = value

    def save_second_strike(self, value):
        self.secondStrike = value

    def is_spare(self):
        return self.get_score() == 10
