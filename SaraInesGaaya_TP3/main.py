import importlib
from os import path
import ui
import animator
importlib.reload(ui)

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = ui.AnimationGenerator()
    tool_window.show()
  
main()

