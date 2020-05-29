import pyxel


class BackGround:
    def __init__(self):
        # ground
        self.cx = pyxel.width/2
        self.cy = pyxel.height/3
        self.speed = 15
        self.number_of_vertical_line = 3
        self.number_of_horizontal_line = 3
        self.v_lines = None
        self.initialize_v_lines()
        distance = self.v_lines[1] - self.v_lines[0]
        self.cycle = distance // self.speed

        h = self.cy / 6
        self.h_lines = [self.cy*2 + i * h
                        for i in [0, 1, 3]]

        # mountain
        self.mnt_speed = 0.1
        self.sx = 0

    def update(self):
        self.update_ground()
        self.update_mountain()

    def update_ground(self):
        if pyxel.frame_count % self.cycle > 0:
            for i in range(len(self.v_lines)):
                vx = self.v_lines[i]
                vx -= self.speed
                self.v_lines[i] = vx
        else:
            self.initialize_v_lines()

    def update_mountain(self):
        self.sx -= self.mnt_speed
        if self.sx < -32:
            self.sx = 0

    def initialize_v_lines(self):
        w = pyxel.width / self.number_of_vertical_line
        n = self.number_of_vertical_line
        self.v_lines = [i * w
                        for i in range(-n-3, n+3)]

    def draw(self):
        pyxel.cls(1)
        self.draw_ground()
        self.draw_mountain()

    def draw_ground(self):
        # horizontal
        for hy in self.h_lines:
            pyxel.line(0, hy, pyxel.width, hy, 3)

        # vertical
        for wx in self.v_lines:
            pyxel.line(self.cx, self.cy, wx, pyxel.height, 3)

        # sky
        pyxel.rect(0, 0, pyxel.width, self.cy*2, 6)

    def draw_mountain(self):
        for i in range(pyxel.width//32+2):
            pyxel.blt(self.sx+32*i, self.cy*2-16, 1, 0, 0, 32, 16, 7)


if __name__ == "__main__":
    pyxel.init(250, 200)
    pyxel.load("../asset.pyxres")
    bg = BackGround()
    pyxel.run(bg.update, bg.draw)
