import importlib
from os import path
import animator
import ui
importlib.reload(ui)
importlib.reload(animator)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = ui.AnimationGenerator()
    tool_window.show()
  
main()

