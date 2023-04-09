from bowling.Frame import Frame, FrameFull


class Game(object):
    NUMBER_OF_FRAMES = 10
    frames = []

    def get_turn(self):
        return len(self.frames)

    def throw(self, value):
        if len(self.frames) == 0:
            frame = Frame()
            frame.add_try(value)
            self.frames.append(frame)
        else:
            try:
                self.frames[-1].add_try(value)
            except FrameFull:
                if len(self.frames) == self.NUMBER_OF_FRAMES:
                    raise Exception('Game is over')
                frame = Frame()
                frame.add_try(value)
                self.frames.append(frame)
