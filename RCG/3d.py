import pyxel
from math import ceil

horizontal_y = 75
ratio = 1.2
roads = [12 if i % 2 else 6 for i in range(100)]
grass = [11 if i % 2 else 3 for i in range(100)]
w0 = 4
h0 = 1
widths = [ceil(w0 * pow(ratio, i)) for i in range(20)]
heights = [ceil(h0 * pow(ratio, i)) for i in range(20)]


def draw_road():
    f = pyxel.frame_count % 20
    w_half = pyxel.width / 2
    y = horizontal_y

    for i in range(19):
        w = widths[i]
        h = heights[i]
        nw = widths[i+1]
        # road
        draw_trapezoid(w_half-w, w_half+w, y,
                       w_half-nw, w_half+nw, y+h, roads[i+f])

        # grass
        draw_trapezoid(0, w_half-w, y,
                       0, w_half-nw, y+h, grass[i+f])
        draw_trapezoid(w_half+w, pyxel.width, y,
                       w_half+nw, pyxel.width, y+h, grass[i+f])
        y += h


def draw_tree():
    f = pyxel.frame_count % 20

    # right
    w = heights[f]
    h = widths[f]
    x = pyxel.width/2 + widths[f] + w
    y = horizontal_y - h
    for i in range(f+1):
        y += heights[i]
    pyxel.rect(x, y, w, h, 9)

    # left
    x = pyxel.width/2 - widths[f] - 2*w
    pyxel.rect(x, y, w, h, 9)


def draw_trapezoid(x1, x2, y1, x3, x4, y2, col):
    """台形
       p1-----p2
      /         \
     /           \
    p3------------p4
    p1(x1, y1)
    p2(x2, y1)
    p3(x3, y2)
    p4(x4, y2)
    """
    pyxel.tri(x1, y1, x2, y1, x3, y2, col)
    pyxel.tri(x2, y1, x3, y2, x4, y2, col)


def update():
    pass


def draw():
    pyxel.cls(1)
    draw_road()
    draw_tree()


if __name__ == "__main__":
    pyxel.init(200, 200, caption="RCG", fps=10)
    pyxel.run(update, draw)
