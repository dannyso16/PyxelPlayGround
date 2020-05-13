from Chip import Chip
import pyxel


class Map:
    SIZE = Chip.IMG_WIDTH  # size of each map chip
    CHIP_WIDTH = Chip.IMG_WIDTH   # 4 map chips in a row
    CHIP_HEIGHT = Chip.IMG_HEIGHT  # 4 map chips in a column

    def __init__(self):
        self.map = self.load_map("map.txt")
        self.MAP_WIDTH = len(self.map[0])
        self.MAP_HEIGHT = len(self.map)
        # print(self.MAP_WIDTH, self.MAP_HEIGHT)

    @classmethod
    def to_screen(cls, i, j):
        """map座標をscreen座標に変換
        """
        return (i * cls.SIZE, j * cls.SIZE)

    @classmethod
    def to_map(cls, x, y):
        i = x // cls.SIZE
        j = y // cls.SIZE
        return (i, j)

    @classmethod
    def draw_chip(cls, i, j, asset_id):
        """map座標(i, j)にasset_idのマップチップを描画
        """
        # Convert to screen coordinates of the chip image
        x, y = cls.to_screen(i, j)
        Chip.draw_asset(x, y, asset_id)

    def draw_map(self):
        for i in range(self.MAP_WIDTH):
            for j in range(self.MAP_HEIGHT):
                asset_id = self.map[j][i]
                self.draw_chip(i, j, asset_id)

    def load_map(self, txt):
        map = []
        map_file = open(txt)
        # Read a line at a time.
        for line in map_file:
            array = []
            data = line.split(",")
            for d in data:
                # Remove extra characters like \n
                s = d.strip()
                if s == "":
                    break
                v = int(d.strip())
                array.append(v)
            map.append(array)

        return map

    def set_map(self, i, j, asset_id):
        # Sets a value at a specified position.
        self.map[j][i] = asset_id

    # Find a specific chip on the map
    def search_map(self, val):
        # Returns the coordinates where the given value exists.
        for j, arr in enumerate(self.map):
            for i, v in enumerate(arr):
                # when found, return the coordinates
                if v == val:
                    return i, j
        raise ValueError(f"val={val} is not found in a map.")

    def is_wall(self, i, j):
        # Check if a given coordinate is a wall
        # outside the map
        if i < 0 or self.MAP_WIDTH <= i:
            return True
        if j < 0 or self.MAP_HEIGHT <= j:
            return True

        # wall
        v = self.map[j][i]
        return Chip.is_wall(v)


# テストして
def update():
    pass


def draw():
    pyxel.cls(12)
    _map.draw_map()
    is_wall = [[] for _ in range(_map.MAP_HEIGHT)]
    for j in range(_map.MAP_HEIGHT):
        for i in range(_map.MAP_WIDTH):
            b = _map.is_wall(i, j)
            is_wall[j].append(b)
    # print(*is_wall, sep="\n")


if __name__ == "__main__":
    _map = Map()

    pyxel.init(_map.MAP_WIDTH*Chip.IMG_WIDTH,
               _map.MAP_HEIGHT*Chip.IMG_HEIGHT)
    pyxel.load("asset.pyxres")

    pyxel.run(update, draw)
