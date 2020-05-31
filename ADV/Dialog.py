import pyxel


class Dialog:
    margin = 1
    padding = 5
    font_height = 6
    line_count = 5
    window_height = line_count*font_height + 2*padding

    def __init__(self):
        super().__init__()

    @classmethod
    def draw(cls, text: str):
        cls._draw_window_frame()
        x = cls.margin + cls.padding
        y = cls.margin + cls.padding
        pyxel.text(x, y, text, 1)

    @classmethod
    def _draw_window_frame(cls):
        x = cls.margin
        y = cls.margin
        w = pyxel.width - 2*cls.margin
        h = cls.window_height
        pyxel.rectb(x, y, w, h, 1)
        pyxel.rect(x+1, y+1, w-2, h-2, 6)
        pyxel.rectb(x+2, y+2, w-4, h-4, 1)


# test
def draw():
    pyxel.cls(12)
    Dialog.draw("Hello\nhello\nworld!")


def update():
    pass


if __name__ == "__main__":
    pyxel.init(200, 200)
    pyxel.run(update, draw)
