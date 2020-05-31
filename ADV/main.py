import pyxel
from Message import Message
from Scene import Scene


class App:
    def __init__(self, debug_mode=True):
        pyxel.init(200, 200, caption="ADV")
        pyxel.mouse(visible=True)

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
        m = Message(x=30, y=120, h=40, w=48, scene_name="room1",
                    flag_name=f"chest",
                    precondition_name=None,
                    text=f"You open the chest.\nNothing in it.")
        messages.append(m)

        m = Message(x=40, y=112, h=8, w=8, scene_name="room1",
                    flag_name=f"portion",
                    precondition_name=None,
                    text=f"This is a portion.\nIt smells bad...")
        messages.append(m)

        m = Message(x=60, y=112, h=8, w=8, scene_name="room1",
                    flag_name=f"meat",
                    precondition_name=None,
                    text=f"This is a meat.\nYou eat it.\nA key is in it.")
        messages.append(m)
        m = Message(x=130, y=90, h=70, w=50, scene_name="room1",
                    flag_name=f"door",
                    precondition_name=f"meat",
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
