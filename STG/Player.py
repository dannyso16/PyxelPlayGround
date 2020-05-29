import pyxel
from Bullet import Bullet


class Player:
    def __init__(self, sx: int, sy: int, height: int, width: int, speed: int,
                 debug_mode=False):
        self.debug_mode = debug_mode

        self.x = sx
        self.y = sy

        # size
        self.width = width
        self.height = height

        self.speed = speed
        self.is_active = True
        self.bullets = []

    def update(self):
        if not self.is_active:
            return
        self.move_with_key()
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.shot()

        for b in self.bullets:
            b.update()

    def draw(self):
        if not self.is_active:
            return
        pyxel.rectb(x=self.x, y=self.y, w=self.width, h=self.height, col=7)

        for b in self.bullets:
            b.draw()

        self.show_debug_info()

    def move_with_key(self):
        nx = self.x
        ny = self.y
        if pyxel.btn(pyxel.KEY_UP):
            ny -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN):
            ny += self.speed
        if pyxel.btn(pyxel.KEY_RIGHT):
            nx += self.speed
        if pyxel.btn(pyxel.KEY_LEFT):
            nx -= self.speed

        if self._can_move_to(nx, ny):
            self.x = nx
            self.y = ny

    def _can_move_to(self, nx: int, ny: int) -> bool:
        w = pyxel.width
        h = pyxel.height
        within_window = (0 <= nx < w) and (0 <= ny < h)
        return within_window

    def shot(self):
        b = Bullet(sx=self.x, sy=self.y, radius=2,
                   speed=-3, color=9, move_function_name='linear')
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
        pyxel.text(0, 0, info, 9)


# test
if __name__ == "__main__":

    pyxel.init(200, 200)
    player = Player(100, 100, 10, 10, 2)
    player.activate()

    def update():
        player.update()

    def draw():
        pyxel.cls(0)
        player.draw()

    pyxel.run(update, draw)
