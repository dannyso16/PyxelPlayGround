import pyxel
from math import sin


class Bullet:
    # TODO: 係数を変えられるようにする
    FUNCTION_LIST = {"linear": lambda x: 0,
                     "sin": lambda x: 10*sin(x/10)}

    def __init__(self, sx: int, sy: int, radius: int, speed: int,
                 color: int, move_function_name: str = "linear"):
        self.sx = sx
        self.sy = sy
        self.x = sx
        self.y = sy
        self.radius = radius
        self.radius_for_collision = 0.8*self.radius
        self.speed = speed
        self.color = color
        self.move_function = Bullet.FUNCTION_LIST[move_function_name]
        # self._vx = 0
        # self._vy = 0
        self.is_active = False

    def update(self):
        self.y += self.speed
        self.x = self.sx + self.move_function(self.y)

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, self.color)

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False


# test
if __name__ == "__main__":
    pyxel.init(200, 200)
    bullet = Bullet(sx=100, sy=100, radius=4, speed=-3, color=3,
                    move_function_name="linear")

    def update():
        bullet.update()

    def draw():
        pyxel.cls(0)
        bullet.draw()

    pyxel.run(update, draw)
