import pyxel
from Enemy import Enemy
from Player import Player
import time


class App:
    def __init__(self):
        # to calcurate frame per second
        self._time = time.time()
        self.fps = 30

        pyxel.init(width=200, height=200, caption="STG",
                   scale=2, fps=30)
        self.player = Player(sx=100, sy=150, speed=2)
        self.player.activate()

        self.enemy = Enemy(sx=100, sy=0, height=10,
                           width=10, speed=0.5, max_hp=5, move_function_name="sin")
        self.enemy.activate()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        self.enemy.update()

        cur_time = time.time()
        self.fps = 1 / (cur_time - self._time)
        self._time = cur_time

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        self.enemy.draw()
        self.show_debug_info()

    def show_debug_info(self):
        info = f"FPS: {self.fps:.2f}\n"
        pyxel.text(0, pyxel.height - 30, info, 9)


if __name__ == "__main__":
    App()
