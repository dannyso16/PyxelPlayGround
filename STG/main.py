import pyxel
from Enemy import Enemy
from Player import Player
from Bullet import Bullet
from Particle import Particle
import time


class App:
    def __init__(self):
        # to calcurate frame per second
        self._time = time.time()
        self.fps = 30

        pyxel.init(width=200, height=200, caption="STG",
                   scale=3, fps=30)
        self.player = Player(sx=100, sy=150, width=10, height=10, speed=2)
        self.player.activate()

        self.enemy = Enemy(sx=100, sy=0, height=10,
                           width=10, speed=0.5, max_hp=10, move_function_name="sin")
        self.enemy.activate()
        self.particles = []
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        self.enemy.update()

        cur_time = time.time()
        self.fps = 1 / (cur_time - self._time)
        self._time = cur_time

        # player bullet と敵との当たり判定
        pb: Bullet
        for pb in self.player.bullets:
            r = pb.radius_for_collision
            cx = pb.x
            cy = pb.y
            ex = self.enemy.x
            ey = self.enemy.y
            ew = self.enemy.width
            eh = self.enemy.height
            if (ex - r < cx < ex + ew + r) and (ey - r < cy < ey + eh + r):
                self.enemy.current_hp -= 1
                if self.enemy.current_hp == 0:
                    self.enemy.deactivate()
                    self.particles.append(Particle(ex, ey))

        # enemy bullet とplayerとの当たり判定
        eb: Bullet
        for eb in self.enemy.bullets:
            r = eb.radius_for_collision
            cx = eb.x
            cy = eb.y
            px = self.player.x
            py = self.player.y
            pw = self.enemy.width
            ph = self.enemy.height
            if (px - r < cx < px + pw + r) and (py - r < cy < py + ph + r):
                self.player.deactivate()
                self.particles.append(Particle(px, py))

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        self.enemy.draw()
        self.show_debug_info()

        p: Particle
        for p in self.particles:
            p.draw()
            if not p.is_active:
                self.particles.remove(p)
                del p

    def show_debug_info(self):
        info = f"FPS: {self.fps:.2f}\n"
        info += f"Particles: {len(self.particles)}\n"
        pyxel.text(0, pyxel.height - 30, info, 9)


if __name__ == "__main__":
    App()
