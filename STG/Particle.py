import pyxel


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frames = self.get_circ_params()
        self.is_active = True

    def update(self):
        pass

    def draw(self):
        if not self.is_active:
            return
        try:
            n = next(self.frames)
            # print(n)
            pyxel.circ(*n)
        except StopIteration:
            self.is_active = False

    def get_circ_params(self):
        circles = [(5, 7), (6, 8), (7, 8), (8, 8),
                   (8, 8), (6, 7), (5, 8), (3, 7)]
        return ((self.x, self.y, r, col) for (r, col) in circles)


# test
if __name__ == "__main__":

    pyxel.init(200, 200)
    p = Particle(100, 100)

    def update():
        p.update()

    def draw():
        pyxel.cls(0)
        p.draw()

    pyxel.run(update, draw)
