import pyxel
from Bullet import Bullet
from math import sin


class Enemy:
    # TODO: 係数を変えられるようにする
    FUNCTION_LIST = {"linear": lambda x: 0,
                     "sin": lambda x: 40*sin(x/20)}

    def __init__(self, sx: int, sy: int, height: int, width: int, speed: int,
                 max_hp: int, move_function_name: str):
        # position
        self.x = sx
        self.y = sy
        self.sx = sx
        self.sy = sy

        # size
        self.width = width
        self.height = height

        self.speed = speed
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.is_active = True
        self.bullets = []
        self.move_function = Enemy.FUNCTION_LIST[move_function_name]

    def update(self):
        if not self.is_active:
            return
        self.move()
        self.shot()

        for b in self.bullets:
            b.update()

    def draw(self):
        if not self.is_active:
            return
        hp_info = f"{self.current_hp}/{self.max_hp}"
        pyxel.text(self.x, self.y - 6, hp_info, 9)
        pyxel.rectb(self.x, self.y, self.width, self.height, 8)

        for b in self.bullets:
            b.draw()

        self.show_debug_info()

    def move(self):
        self.y += self.speed
        self.x = self.sx + self.move_function(self.y)

    def shot(self):
        if pyxel.frame_count % 40 == 0:
            b = Bullet(sx=self.x, sy=self.y, radius=2,
                       speed=3, color=8, move_function_name='linear')
            self.bullets.append(b)

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def show_debug_info(self):
        info = f"len(bullets): {len(self.bullets)}\n"
        info += f"x={self.x:.2f}, y={self.y:.2f}\n"
        pyxel.text(pyxel.width-80, 0, info, 9)


# test
if __name__ == "__main__":

    pyxel.init(200, 200)
    enemy = Enemy(sx=100, sy=0, height=10, width=10, speed=0.5, max_hp=5,
                  move_function_name="sin")
    enemy.activate()

    def update():
        enemy.update()

    def draw():
        pyxel.cls(0)
        enemy.draw()

    pyxel.run(update, draw)
