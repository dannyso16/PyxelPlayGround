import pyxel
from Map import Map
from Chip import Chip


class Player:

    _DIRECTIONS = ["N", "E", "W", "S"]
    MOVE_SPEED = 1
    offset = 1

    def __init__(self, map: Map):
        self.x = 0
        self.y = 0
        self.direction = "S"
        self.map = map

    def update(self):
        self.move_with_key()

    def draw(self):
        asset_id = self._get_asset_id()
        Chip.draw_asset(self.x, self.y, asset_id)

    def _change_direction(self, direction: str):
        assert direction in self._DIRECTIONS, "方角はNEWSのいずれかにしてください"
        self.direction = direction

    def _get_asset_id(self) -> int:
        asset_ids = {"N": 3, "E": 1, "W": 2, "S": 0}
        return asset_ids[self.direction]

    def _can_move_to(self, x, y):
        w = Chip.IMG_WIDTH - self.offset
        h = Chip.IMG_HEIGHT - self.offset
        corners = [(x, y), (x+w, y), (x, y+h), (x+w, y+h)]
        for (cx, cy) in corners:
            i, j = Map.to_map(cx, cy)
            if self.map.is_wall(i, j):
                return False
        return True

    def move_with_key(self):
        nx = self.x
        ny = self.y
        if pyxel.btn(pyxel.KEY_UP):
            ny -= self.MOVE_SPEED
            self._change_direction("N")
        if pyxel.btn(pyxel.KEY_DOWN):
            ny += self.MOVE_SPEED
            self._change_direction("S")
        if pyxel.btn(pyxel.KEY_RIGHT):
            nx += self.MOVE_SPEED
            self._change_direction("E")
        if pyxel.btn(pyxel.KEY_LEFT):
            nx -= self.MOVE_SPEED
            self._change_direction("W")

        if self._can_move_to(nx, ny):
            self.x = nx
            self.y = ny


# テスト
def update():
    pc.update()


def draw():
    pyxel.cls(12)
    _map.draw_map()
    pc.draw()


if __name__ == "__main__":
    _map = Map()

    pyxel.init(_map.MAP_WIDTH*Chip.IMG_WIDTH,
               _map.MAP_HEIGHT*Chip.IMG_HEIGHT)
    pyxel.load("asset.pyxres")
    pc = Player(_map)
    pyxel.run(update, draw)
