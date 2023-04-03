class Frame(object):
    firstTry = 0
    secondTry = 0

    def get_score(self):
        return self.firstTry + self.secondTry

    def save_first_try(self, value):
        self.firstTry = value

    def save_second_try(self, value):
        self.secondTry = value

    def is_spare(self):
        return self.get_score() == 10

    def is_strike(self):
        return self.firstTry == 10
