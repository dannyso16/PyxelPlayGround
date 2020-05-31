from enum import Enum, auto
import pyxel
from Message import Message


class State(Enum):
    SEARCH = auto()
    MESSAGE = auto()
    CLEAR = auto()


class Scene:

    def __init__(self, messages: "list[Message]"):
        self.messages = messages
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
        m: Message
        for m in self.messages:
            m.draw()


if __name__ == "__main__":
    pyxel.init(200, 200)
    messages = []
    for i in range(3):
        m = Message(x=10+60*i, y=80, h=70, w=50, scene_name="test",
                    text=f"text_No.{i}")
        messages.append(m)

    scene = Scene(messages)
    pyxel.run(scene.update, scene.draw)