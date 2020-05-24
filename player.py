import pyxel
from Map import Map
from Chip import Chip
from Dialog import Dialog


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
        self.act_with_key()

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

    def _get_forward_map_pos(self) -> tuple:
        """前方のmap座標を取得
        """
        cx, cy = Chip.get_center(self.x, self.y)
        h = Chip.IMG_HEIGHT
        w = Chip.IMGBANK_WIDTH
        if self.direction == "N":
            cy -= h
        elif self.direction == "E":
            cx += w
        elif self.direction == "W":
            cx -= w+1  # TODO: 統一的に書いてほしい
        else:
            cy += h

        (i, j) = Map.to_map(cx, cy)
        return (i, j)

    def _check_forward(self) -> int:
        """前方を調べ、何があるかを返す
        """
        (i, j) = self._get_forward_map_pos()
        return self.map.get_asset_id(i, j)

    def act_with_key(self):
        """調べたりする
        """
        # 押下時のみ反応させる
        if pyxel.btn(pyxel.KEY_SPACE):
            asset_id = self._check_forward()
            # 敵
            if Chip.is_enemy(asset_id):
                Dialog.draw("Enemy")
            # アイテム
            elif Chip.is_item(asset_id):
                Dialog.draw("Item")
                # 何かする
                # (i, j) = self._get_forward_map_pos()
                # self.map.set_map(i, j, 10)
            # カベ
            elif Chip.is_wall(asset_id):
                Dialog.draw("Wall")

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
