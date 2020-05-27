import pyxel


class Functions:
    def __init__(self):
        pass

    @classmethod
    def get_invader(cls, sx: int, sy: int, w: int, h: int):
        w_stride = pyxel.width / w
        h_stride = pyxel.height / h

        t = list(range(w*h))
        _y = [(ti // w) for ti in t]
        x = [(ti % w) * w_stride if yi % 2 == 0
             else (w - 1 - ti % w) * w_stride
             for ti, yi in zip(t, _y)]
        y = [yi * h_stride for yi in _y]
        return zip(x, y)

    @classmethod
    def get_linear(cls, a: int, b: int, c: int):
        """return ax + by + c = 0
        """
        if a == 0:
            pass


# text
if __name__ == "__main__":
    pyxel.init(200, 200)
    xy = Functions.get_invader(sx=10, sy=10,
                               w=30, h=30)

    def update():
        pass

    def draw():
        pyxel.cls(0)
        try:
            x, y = next(xy)
            pyxel.circb(x, y, 10, 6)
            pyxel.text(10, 10, f"x={x:.1f}, y={y:.1f}", 8)
        except StopIteration:
            pyxel.text(0, 0, "Ended", 7)

    pyxel.run(update, draw)
