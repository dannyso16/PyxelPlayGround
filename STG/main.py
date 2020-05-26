import pyxel
from Enemy import Enemy
from Player import Player


class App:
    def __init__(self):
        pyxel.init(200, 200)
        self.player = Player(sx=100, sy=150, speed=2)
        self.player.activate()

        self.enemy = Enemy(sx=100, sy=0, height=10,
                           width=10, speed=0.5, max_hp=5, move_function_name="sin")
        self.enemy.activate()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        self.enemy.update()

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        self.enemy.draw()


if __name__ == "__main__":
    App()
