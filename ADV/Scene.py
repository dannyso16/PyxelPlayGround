from enum import Enum, auto
import pyxel
from Message import Message


class State(Enum):
    SEARCH = auto()
    MESSAGE = auto()
    CLEAR = auto()


class Scene:

    def __init__(self, messages: "list[Message]",
                 debug_mode=True):
        self.messages = messages
        self.debug_mode = debug_mode
        self.flags = {}
        m: Message
        for m in self.messages:
            self.flags[m.flag_name] = False
        self.state = State.SEARCH

    def update(self):
        m: Message
        for m in self.messages:
            m.update()

    def draw(self):
        if self.debug_mode:
            self.show_debug_info()

        m: Message
        for m in self.messages:
            m.draw()

    def click_mouse(self):
        clicked_flags = []
        m: Message
        for m in self.messages:
            if m.on_the_mouse:
                m.toggle_state()
                self.flags[m.flag_name] = True
                clicked_flags.append(m.flag_name)

        for m in self.messages:
            for name in clicked_flags:
                if m.precondition_name == name:
                    m.activate()

    def show_debug_info(self):
        info = f"Msgs: {len(self.messages)}\n"
        info += f"msgs"
        for m in self.messages:
            info += f"{m.state}\n"
        info += f"flags:\n"
        for k, v in self.flags.items():
            info += f"{k}: {v}\n"
        pyxel.text(0, 0, info, 8)


if __name__ == "__main__":
    pyxel.init(200, 200)
    pyxel.mouse(visible=True)
    messages = []
    for i in range(3):
        m = Message(x=10+60*i, y=80, h=70, w=50, scene_name="test",
                    flag_name=f"flag{i}",
                    text=f"text_No.{i}")
        messages.append(m)

    scene = Scene(messages)
    pyxel.run(scene.update, scene.draw)
