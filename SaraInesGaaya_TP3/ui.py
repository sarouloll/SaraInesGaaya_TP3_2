import sys
from maya import cmds
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget, QGridLayout, QPushButton, QSpinBox, QLabel, QApplication, QHBoxLayout )

class AnimationGenerator(QWidget):
    def __init__(self):
        super(). __init__()

        self.setWindowTitle("Random Animator Generator")
        self.setMinimumWidth(350)
        self.setMinimumHeight(600)

        self.create_ui()
        #self.add_to_widget()

    def create_ui(self):
        
        self.create_button = QPushButton("Create")
        #widget = QWidget()
        #widget.setLayout(layout)
        #self.setCentralWidget(widget)

        layout = QGridLayout(self)
        spinbox = QSpinBox(self)
        spinbox.setRange(0, 100)

        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        self.duration = QtWidgets.QSpinBox
        self.step = QtWidgets.QSpinBox

        self.translate_min_x = QtWidgets.QSpinBox
        self.translate_min_y = QtWidgets.QSpinBox
        self.translate_min_z = QtWidgets.QSpinBox
        self.translate_max_x = QtWidgets.QSpinBox
        self.translate_max_y = QtWidgets.QSpinBox
        self.translate_max_z = QtWidgets.QSpinBox

        self.rotate_min_x = QtWidgets.QSpinBox
        self.rotate_min_y = QtWidgets.QSpinBox
        self.rotate_min_z = QtWidgets.QSpinBox
        self.rotate_max_x = QtWidgets.QSpinBox
        self.rotate_max_y = QtWidgets.QSpinBox
        self.rotate_max_z = QtWidgets.QSpinBox

        self.scale_min_x = QtWidgets.QSpinBox
        self.scale_min_y = QtWidgets.QSpinBox
        self.scale_min_z = QtWidgets.QSpinBox
        self.scale_max_x = QtWidgets.QSpinBox
        self.scale_max_y = QtWidgets.QSpinBox
        self.scale_max_z = QtWidgets.QSpinBox


        

        self.obj = QtWidgets.QLineEdit("")
        # self.posX = QtWidgets.QLineEdit("")
        # self.posY = QtWidgets.QLineEdit("")
        # self.posZ = QtWidgets.QLineEdit("")
        # self.scale = QtWidgets.QLineEdit("")

        # self.posX_max = QtWidgets.QLineEdit("")
        # self.posY_max = QtWidgets.QLineEdit("")
        # self.posZ_max = QtWidgets.QLineEdit("")
        # self.scale_max = QtWidgets.QLineEdit("")

        #self.obj.setFixedSize(100, 25)
        # self.posX.setFixedSize(100, 25)
        # self.posY.setFixedSize(100, 25)
        # self.posZ.setFixedSize(100, 25)
        # self.scale.setFixedSize(100, 25)

        # self.posX_max.setFixedSize(100, 25)
        # self.posY_max.setFixedSize(100, 25)
        # self.posZ_max.setFixedSize(100, 25)
        # self.scale_max.setFixedSize(100, 25)
        

        layout.addWidget(QLabel("Duration (Frames)"), 1, 0)
        layout.addWidget(QLabel('Steps (Frames)'), 2, 0)
        # layout.addWidget(QLabel('Position Y'), 7, 0)
        # layout.addWidget(QLabel('Position Z'), 9, 0)
        # layout.addWidget(QLabel('Scale'), 11, 0)
        # layout.addWidget(QLabel('min'), 3, 1)
        # layout.addWidget(QLabel('max'), 3, 2)

        #layout.addWidget(self.obj, 1, 1)
        # layout.addWidget(self.posX, 5, 1)
        # layout.addWidget(self.posY, 7, 1)
        # layout.addWidget(self.posZ, 9, 1)
        # layout.addWidget(self.scale, 11, 1)

        # layout.addWidget(self.posX_max, 5, 2)
        # layout.addWidget(self.posY_max, 7, 2)
        # layout.addWidget(self.posZ_max, 9, 2)
        # layout.addWidget(self.scale_max, 11, 2)

        layout.addWidget(self.create_button)






    # #def add_to_widget(self):

    #     self.layout.addWidget(QLabel("Duration (Frames)"), 1, 0)
    #     self.layout.addWidget(QLabel('Step (Frames)'), 5, 0)

    #     self.layout.addWidget(self.duration, 1, 1)
    #     self.layout.addWidget(self.step, 5, 1)

        


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = AnimationGenerator()
    tool_window.show()

main()

app = QApplication(sys.argv)
app.exec()