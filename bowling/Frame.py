class FrameFull(Exception):
    """Raised when a new attempt is added but the frame is full."""
    pass


class Frame:
    firstTry = -1
    secondTry = -1

    def get_score(self):
        return self.firstTry + self.secondTry

    def save_first_try(self, value):
        self.firstTry = value

    def save_second_try(self, value):
        self.secondTry = value

    def add_try(self, value):
        if self.firstTry == -1:
            self.save_first_try(value)
        elif self.secondTry == -1 and not self.is_strike():
            self.save_second_try(value)
        else:
            raise FrameFull('The frame is full')

    def is_spare(self):
        return self.get_score() == 10

    def is_strike(self):
        return self.firstTry == 10
