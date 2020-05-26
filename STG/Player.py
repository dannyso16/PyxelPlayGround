import pyxel
from Bullet import Bullet


class Player:
    def __init__(self, sx: int, sy: int, speed: int):
        self.x = sx
        self.y = sy
        self.radius_for_collision = 4
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
        pyxel.circb(self.x, self.y, 4, 7)

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
        b = Bullet(sx=self.x, sy=self.y, radius=4,
                   speed=-3, color=5, move_function_name='linear')
        self.bullets.append(b)

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def show_debug_info(self):
        info = f"len(bullets): {len(self.bullets)}\n"
        info += f"x={self.x}, y={self.y}\n"
        pyxel.text(0, 0, info, 9)


# test
if __name__ == "__main__":

    pyxel.init(200, 200)
    player = Player(100, 100, 2)
    player.activate()

    def update():
        player.update()

    def draw():
        pyxel.cls(0)
        player.draw()

    pyxel.run(update, draw)
