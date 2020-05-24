import pyxel


class Chip:
    # 画像バンクの各画像に関するクラス
    # asset.pyxres の中身
    # in image bank 0
    #  [ 0][ 1][ 2][ 3]
    #  [ 4][ 5][ 6][ 7]
    #  [ 8][ 9][10][11]
    #  [12][13][14][15]

    ASSET_ID = {"pc_front": 0,
                "pc_right": 1,
                "pc_left": 2,
                "pc_back": 3,
                "npc_a": 4,
                "npc_b": 5,
                "npc_c": 6,
                "item_a": 7,
                "item_b": 8,
                "item_c": 9,
                "tile_grass": 10,
                "tile_ground": 11,
                "tile_sky": 12,
                "wall_corner": 13,
                "wall_edge": 14,
                "wall_alone": 15}

    # image bank の大きさ
    IMGBANK_WIDTH = 4
    IMGBANK_HEIGHT = 4

    # 各画像の大きさ
    IMG_WIDTH = 8
    IMG_HEIGHT = 8

    @classmethod
    def draw_asset(cls, x: int, y: int, asset_id: int, background_id: int = 10):
        """ asset_id の画像を(x, y)に描画
        """
        assert 0 <= asset_id <= 15, "asset_id は0～15で指定"
        # asset はすべて白色(7)で透過
        # 背景を描画
        u = (background_id % cls.IMGBANK_WIDTH) * cls.IMG_WIDTH
        v = (background_id // cls.IMGBANK_WIDTH) * cls.IMG_HEIGHT
        pyxel.blt(x, y, 0, u, v, cls.IMG_WIDTH, cls.IMG_HEIGHT, 7)

        # assetを描画
        u = (asset_id % cls.IMGBANK_WIDTH) * cls.IMG_WIDTH
        v = (asset_id // cls.IMGBANK_WIDTH) * cls.IMG_HEIGHT
        pyxel.blt(x, y, 0, u, v, cls.IMG_WIDTH, cls.IMG_HEIGHT, 7)

    @classmethod
    def get_center(cls, x: int, y: int) -> tuple:
        cx = x + cls.IMG_WIDTH//2
        cy = y + cls.IMG_HEIGHT//2
        return (cx, cy)

    @classmethod
    def is_wall(cls, asset_id):
        no_collidables = [10, 11, 12]  # 背景
        # 背景はfalse, それ以外はtrue
        return asset_id not in no_collidables

    @classmethod
    def is_pc(cls, asset_id):
        pc = [0, 1, 2, 3]
        return asset_id in pc

    @classmethod
    def is_enemy(cls, asset_id):
        npc = [4, 5, 6]
        return asset_id in npc

    @classmethod
    def is_item(cls, asset_id):
        item = [7, 8, 9]
        return asset_id in item


# 以下テスト用
def update():
    pass


def draw():
    pyxel.cls(0)
    i = pyxel.frame_count//5 % 4
    Chip.draw_asset(0, 0, i)
    # print(Chip.is_wall(i))


if __name__ == "__main__":
    pyxel.init(80, 80)
    pyxel.load("asset.pyxres")
    pyxel.run(update, draw)
