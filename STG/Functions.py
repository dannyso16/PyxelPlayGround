import pyxel


class Functions:
    def __init__(self):
        pass

    @classmethod
    def get_invader(cls, start_idx: int, w: int, h: int, frame_count: int):
        """return invader-like movement
        ex. w=5, h=3, start_idx=2
                     2 ->  3 ->  4
         9 <-  8 <-  7 <-  6 <-  5
        10 -> 11 -> 12 -> 13 -> 14

        frame_countを指定：そのフレームでの座標(x, y)を返す
        """
        w_stride = pyxel.width / w
        h_stride = pyxel.height / h

        t = start_idx + frame_count
        _y = t // w
        if _y % 2 == 0:
            x = (t % w) * w_stride
        else:
            x = (w - 1 - t % w) * w_stride
        y = _y * h_stride
        return (x, y)

    @classmethod
    def get_linear(cls, sx: int, sy: int, a: int, b: int, c: int, frame_count: int):
        """return ax + by + c = 0
        """
        if a == 0:
            pass

    @classmethod
    def get_sin(cls, sx: int, sy: int, a: int, omega: int, frame_count: int):
        """return y = a * sin(omega * x)
        """
        pass


# text
if __name__ == "__main__":
    pyxel.init(200, 200)

    def get_invader(start_idx, frame_count):
        return Functions.get_invader(start_idx=start_idx, w=10, h=10,
                                     frame_count=frame_count)

    num_of_invaders = 30

    def update():
        pass

    def draw():
        pyxel.cls(0)
        for i in range(num_of_invaders):
            x, y = get_invader(i, pyxel.frame_count//2)
            pyxel.circb(x, y, 10, 6)
            pyxel.text(10, i*6, f"x={x:.1f}, y={y:.1f}", 8)

    pyxel.run(update, draw)
