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
        self.draw_function = draw_function
        self.flag_name = flag_name
        self.debug_mode = debug_mode

    def update(self):
        pass

    def draw(self):
        self.draw_function()

        if self.debug_mode:
            pyxel.rectb(self.x, self.y, self.w, self.h, 8)


if __name__ == "__main__":
    pyxel.init(200, 200)

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
