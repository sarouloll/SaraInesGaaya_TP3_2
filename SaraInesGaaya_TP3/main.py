import importlib
import os
import sys

# Trouve manuellement le path pour éviter les erreurs de communications entre modules
a_path = os.path.abspath(__file__)
a_folder_path = os.path.dirname(a_path)
sys.path.append(a_folder_path)

# Imports de modules, doit mettre après le folder path sinon erreur 
import animator
import ui
importlib.reload(ui)
importlib.reload(animator)


# Éxécution principale du programme
def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = ui.AnimationGenerator()
    tool_window.show()
  
main()

