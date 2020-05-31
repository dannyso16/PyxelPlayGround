import pyxel


class App:

    ROW = 5
    COLUMN = 5

    def __init__(self,
                 debug_mode=True):
        pyxel.init(200, 200, caption="PZL")
        pyxel.mouse(visible=True)

        self.debug_mode = debug_mode

        self.matrix = [[False]*App.COLUMN for _ in range(App.ROW)]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON):
            self.light_cell(pyxel.mouse_x, pyxel.mouse_y)

    def draw(self):
        pyxel.cls(1)
        self.draw_matrix()
        self.draw_info()
        self.draw_reset_btn()

    def draw_matrix(self):
        margin = 8
        width = 32
        for j in range(App.ROW):
            for i in range(App.COLUMN):
                col = 7 if self.matrix[j][i] else 5
                x = margin + i*width
                y = margin + j*width
                pyxel.rect(x, y, width, width, col)
                pyxel.rectb(x, y, width, width, 1)

    def draw_info(self):
        margin = 8
        info = "TIME:\n"
        info += f"{0}\n\n"
        info += f"COUNT:\n"
        info += f"{0}"
        pyxel.text(pyxel.width-30, margin, info, 11)

    def draw_reset_btn(self):
        margin = 8
        width = 32
        x = margin
        y = 2 * margin + width * App.ROW
        pyxel.rect(x, y, width, 20, 1)
        pyxel.rectb(x, y, width, 20, 11)
        padding = 6
        pyxel.text(x+padding, y+padding, "RESET", 11)

    def light_cell(mx, my):
        if not self.in_matrix(mx, my):
            return

    def in_matrix(mx, my):
        return True


if __name__ == "__main__":
    App()
