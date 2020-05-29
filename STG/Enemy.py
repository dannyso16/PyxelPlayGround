import pyxel
from Bullet import Bullet
from Functions import Functions
from math import sin


class Enemy:

    def __init__(self, sx: int, sy: int, height: int, width: int, speed: int,
                 max_hp: int, idx: int, debug_mode=False):
        self.debug_mode = debug_mode

        # position
        self.x = sx
        self.y = sy
        self.sx = sx
        self.sy = sy

        # size
        self.width = width
        self.height = height

        self.idx = idx
        self.speed = speed
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.is_active = True
        self.bullets = []

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
        def get_invader(frame_count):
            return Functions.get_invader(self.idx, 10, 10, frame_count)

        f = pyxel.frame_count // (30 / self.speed)
        x, y = get_invader(f)
        self.y = y
        self.x = x

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
        if not self.debug_mode:
            return
        info = f"len(bullets): {len(self.bullets)}\n"
        info += f"x={self.x:.2f}, y={self.y:.2f}\n"
        pyxel.text(pyxel.width-80, 0, info, 9)


# test
if __name__ == "__main__":

    pyxel.init(200, 200)
    enemy = Enemy(sx=100, sy=0, height=10, width=10, speed=0.5, max_hp=5,
                  idx=0)
    enemy.activate()

    def update():
        enemy.update()

    def draw():
        pyxel.cls(0)
        enemy.draw()

    pyxel.run(update, draw)
