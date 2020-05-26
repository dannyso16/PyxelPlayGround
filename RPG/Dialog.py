import pyxel


class Dialog:
    margin = 1
    padding = 5
    font_height = 6
    line_count = 1
    window_height = line_count*font_height + 2*padding

    def __init__(self):
        super().__init__()

    @classmethod
    def draw(cls, text: str):
        cls._draw_window_frame()
        x = cls.margin + cls.padding
        y = pyxel.height - cls.window_height - cls.margin + cls.padding
        pyxel.text(x, y, text, 5)

    @classmethod
    def _draw_window_frame(cls):
        x = cls.margin
        y = pyxel.height - cls.window_height - cls.margin
        w = pyxel.width - 2*cls.margin
        h = cls.window_height
        pyxel.rectb(x, y, w, h, 0)
        pyxel.rect(x+1, y+1, w-2, h-2, 7)
        pyxel.rectb(x+2, y+2, w-4, h-4, 0)


# test
def draw():
    pyxel.cls(12)
    Dialog.draw("Hello\nhello\nworld!")


def update():
    pass


if __name__ == "__main__":
    pyxel.init(50, 50)
    pyxel.run(update, draw)
