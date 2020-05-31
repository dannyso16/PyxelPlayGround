import pyxel
from Message import Message
from Scene import Scene


class App:
    def __init__(self, debug_mode=True):
        pyxel.init(200, 200, caption="ADV")
        pyxel.mouse(visible=True)

        self.debug_mode = debug_mode

        messages = []
        for i in range(3):
            m = Message(x=10+60*i, y=80, h=70, w=50, scene_name="test",
                        text=f"text_No.{i}")
            messages.append(m)

        self.scene = Scene(messages)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.scene.update()

        if pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON):
            self.scene.click_mouse()

    def draw(self):
        pyxel.cls(0)
        self.scene.draw()
        self.debug_info()

    def debug_info(self):
        if not self.debug_mode:
            return
        info = f"mouse x:{pyxel.mouse_x:.1f}, y:{pyxel.mouse_y:.1f}"
        pyxel.text(0, 0, info, 7)


if __name__ == "__main__":
    App()
