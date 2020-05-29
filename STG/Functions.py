import pyxel


class Functions:
    def __init__(self):
        pass

    @classmethod
    def get_invader(cls, start_idx: int, w: int, h: int):
        """return invader-like movement
        ex. w=5, h=3, start_idx=2
                     2 ->  3 ->  4 
         9 <-  8 <-  7 <-  6 <-  5
        10 -> 11 -> 12 -> 13 -> 14
        """
        w_stride = pyxel.width / w
        h_stride = pyxel.height / h

        t = list(range(start_idx, w*h))
        _y = [(ti // w) for ti in t]
        x = [(ti % w) * w_stride if yi % 2 == 0
             else (w - 1 - ti % w) * w_stride
             for ti, yi in zip(t, _y)]
        y = [yi * h_stride for yi in _y]
        return zip(x, y)

    @classmethod
    def get_linear(cls, sx: int, sy: int, a: int, b: int, c: int):
        """return ax + by + c = 0
        """
        if a == 0:
            pass

    @classmethod
    def get_sin(cls, sx: int, sy: int, a: int, omega: int):
        """return y = a * sin(omega * x) 
        """
        pass


# text
if __name__ == "__main__":
    pyxel.init(200, 200)
    invaders = []
    for i in range(30):
        invader = Functions.get_invader(start_idx=i, w=10, h=10)
        invaders.append(invader)

    def update():
        pass

    def draw():
        pyxel.cls(0)
        for i, invader in enumerate(invaders):
            try:
                x, y = next(invader)
                pyxel.circb(x, y, 10, 6)
                pyxel.text(10, i*6, f"x={x:.1f}, y={y:.1f}", 8)
            except StopIteration:
                pyxel.text(0, 0, "Ended", 7)

    pyxel.run(update, draw)
