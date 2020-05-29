import pyxel
from Enemy import Enemy
from Player import Player
from Bullet import Bullet
from Particle import Particle
from BackGround import BackGround
import time


class App:
    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

        # to calcurate frame per second
        self._time = time.time()
        self.fps = 30

        pyxel.init(width=250, height=200, caption="STG",
                   scale=3, fps=30)
        pyxel.load("../asset.pyxres")

        self.player = Player(sx=100, sy=150, width=10, height=10, speed=2,
                             debug_mode=self.debug_mode)
        self.player.activate()
        self.enemies = []
        for i in range(20):
            e = Enemy(sx=100, sy=0, height=10,
                      width=10, speed=0.5, max_hp=10, idx=i,
                      debug_mode=self.debug_mode)
            e.activate()
            self.enemies.append(e)

        self.particles = []

        self.back_ground = BackGround()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.back_ground.update()
        self.player.update()
        for e in self.enemies:
            e.update()

        cur_time = time.time()
        self.fps = 1 / (cur_time - self._time)
        self._time = cur_time

        # player bullet と敵との当たり判定
        pb: Bullet
        for pb in self.player.bullets:
            r = pb.radius_for_collision
            cx = pb.x
            cy = pb.y
            for enemy in self.enemies:
                ex = enemy.x
                ey = enemy.y
                ew = enemy.width
                eh = enemy.height
                if (ex - r < cx < ex + ew + r) and (ey - r < cy < ey + eh + r):
                    enemy.current_hp -= 1
                    if enemy.current_hp == 0:
                        self.enemies.remove(enemy)
                        enemy.deactivate()
                        self.particles.append(Particle(ex, ey))

        # enemy bullet とplayerとの当たり判定
        if not self.player.is_active:
            return
        eb: Bullet
        for enemy in self.enemies:
            for eb in enemy.bullets:
                r = eb.radius_for_collision
                cx = eb.x
                cy = eb.y
                px = self.player.x
                py = self.player.y
                pw = enemy.width
                ph = enemy.height
                if (px - r < cx < px + pw + r) and (py - r < cy < py + ph + r):
                    self.player.deactivate()
                    self.particles.append(Particle(px, py))

    def draw(self):
        self.back_ground.draw()
        self.player.draw()
        for e in self.enemies:
            e.draw()
        self.show_debug_info()

        p: Particle
        for p in self.particles:
            p.draw()
            if not p.is_active:
                self.particles.remove(p)
                del p

    def show_debug_info(self):
        if not self.debug_mode:
            return
        info = f"FPS: {self.fps:.2f}\n"
        info += f"Particles: {len(self.particles)}\n"
        pyxel.text(0, pyxel.height - 30, info, 9)


if __name__ == "__main__":
    App()
