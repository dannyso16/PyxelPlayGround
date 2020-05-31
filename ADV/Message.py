import pyxel


class Message:

    def __init__(self, x: int, y: int, h: int, w: int,
                 scene_name: str, text: str,
                 draw_function: "function" = None,
                 flag_name: str = None,
                 debug_mode=True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.scene_name = scene_name
        self.text = text
        if draw_function:
            self.draw_function = draw_function
        else:
            self.draw_function = self.default_draw_function
        self.flag_name = flag_name
        self.on_the_mouse = False
        self.debug_mode = debug_mode

    def update(self):
        if self.is_reachable(pyxel.mouse_x, pyxel.mouse_y):
            self.on_the_mouse = True
        else:
            self.on_the_mouse = False

    def draw(self):
        self.draw_function()

        if self.debug_mode:
            col = 8 if self.on_the_mouse else 0
            pyxel.rectb(self.x, self.y, self.w, self.h, col)

    def is_reachable(self, mx: int, my: int) -> bool:
        """(mx, my)がMessage object内かどうか判定
        """
        b = self.x < mx < self.x + self.w
        b &= self.y < my < self.y + self.h
        return b

    def default_draw_function(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 0)


if __name__ == "__main__":
    pyxel.init(200, 200)
    pyxel.mouse(visible=True)

    def draw_function():
        pyxel.rect(10, 80, 50, 70, 12)
        pyxel.rect(15, 85, 40, 27, 13)
        pyxel.rectb(15, 85, 40, 27, 5)
        pyxel.rect(15, 117, 40, 27, 13)
        pyxel.rectb(15, 117, 40, 27, 5)
        pyxel.circ(50, 114, 2, 9)

    message = Message(x=10, y=80, h=70, w=50, scene_name="hoge",
                      text="this is a pen", draw_function=draw_function)

    pyxel.run(message.update, message.draw)
