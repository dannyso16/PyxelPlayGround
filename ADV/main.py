import pyxel
from Message import Message
from Scene import Scene


class App:
    def __init__(self, debug_mode=True):
        pyxel.init(200, 200, caption="ADV")
        pyxel.mouse(visible=True)
        pyxel.load("../asset.pyxres")

        self.debug_mode = debug_mode

        messages = self.get_messages()

        self.scene = Scene(messages)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.scene.update()

        if pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON):
            self.scene.click_mouse()

    def draw(self):
        self.draw_back_ground()
        self.scene.draw()
        self.debug_info()

    def draw_back_ground(self):
        pyxel.cls(15)
        h = pyxel.height/5
        pyxel.rect(0, 4*h, pyxel.width, h, 4)

    def get_messages(self):
        messages = []

        def draw_chest():
            pyxel.blt(x=30, y=136, img=0, u=0, v=32, w=48, h=24, colkey=7)

        m = Message(x=30, y=136, h=24, w=48, scene_name="room1",
                    flag_name=f"chest",
                    precondition_name=None,
                    draw_function=draw_chest,
                    text=f"You open the chest.\nNothing in it.")
        messages.append(m)

        def draw_potion():
            pyxel.blt(x=40, y=128, img=0, u=8, v=16, w=8, h=8, colkey=7)

        m = Message(x=40, y=128, h=8, w=8, scene_name="room1",
                    flag_name=f"portion",
                    precondition_name=None,
                    draw_function=draw_potion,
                    text=f"This is a portion.\nIt smells bad...")
        messages.append(m)

        def draw_meat():
            pyxel.blt(x=60, y=128, img=0, u=24, v=8, w=8, h=8, colkey=7)

        m = Message(x=60, y=128, h=8, w=8, scene_name="room1",
                    flag_name=f"meat",
                    precondition_name=None,
                    draw_function=draw_meat,
                    text=f"This is a meat.\nYou eat it.\nA key is in it.")
        messages.append(m)

        def draw_door():
            x, y = 130, 90
            w, h = 50, 70
            pyxel.rect(x, y, w, h, 12)
            pyxel.rect(x+5, y+5, w-10, h//2-10, 13)
            pyxel.rectb(x+5, y+5, w-10, h//2-10, 5)
            pyxel.rect(x+5, y+h//2+5, w-10, h//2-10, 13)
            pyxel.rectb(x+5, y+h//2+5, w-10, h//2-10, 5)
            pyxel.circ(x + 3*w//4, y+h//2, 2, 9)

        m = Message(x=130, y=90, h=70, w=50, scene_name="room1",
                    flag_name=f"door",
                    precondition_name=f"meat",
                    draw_function=draw_door,
                    text=f"You unlock the door.\nWell done!")
        messages.append(m)
        return messages

    def debug_info(self):
        if not self.debug_mode:
            return
        info = f"mouse x:{pyxel.mouse_x:.1f}, y:{pyxel.mouse_y:.1f}"
        pyxel.text(0, 0, info, 7)


if __name__ == "__main__":
    App()
