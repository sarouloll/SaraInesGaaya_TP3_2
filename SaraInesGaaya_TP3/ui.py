import animator
from PySide6.QtWidgets import (QWidget, QGridLayout, QPushButton, QSpinBox, QLabel, QGroupBox )

class AnimationGenerator(QWidget):
    def __init__(self):
        super(). __init__()

        # Configuration standard de la fenêtre
        self.setWindowTitle("Random Animator Generator")
        self.setMinimumWidth(450)
        self.setMinimumHeight(600)
        self.layout = QGridLayout(self)

        # Fonctions à ajouter à la fenêtre
        self.animation_timing()
        self.translate_parameters()
        self.rotate_parameters()
        self.scale_parameters()
        # Ajout du bouton de création et liaison 
        self.create_button = QPushButton("Create")
        self.layout.addWidget(self.create_button)
        self.create_button.clicked.connect(self.on_clicked)


    def animation_timing(self):
        animation = QGroupBox("Animation timing")
        animation_layout = QGridLayout(animation)

        self.duration = QSpinBox()
        self.duration.setRange(0, 500)

        self.step = QSpinBox()
        self.step.setRange(0, 500)

        animation_layout.addWidget(QLabel("Duration (Frames):"), 0, 0)
        animation_layout.addWidget(self.duration, 0, 1)
        animation_layout.addWidget(QLabel("Steps (Frames):"), 0, 2)
        animation_layout.addWidget(self.step, 0, 3)

        self.layout.addWidget(animation)
        

    def translate_parameters(self):
        translate = QGroupBox("Translate Parameters")
        translate_layout = QGridLayout(translate)

        self.translate_minX = QSpinBox()
        self.translate_minX.setRange(0, 500)

        self.translate_minY = QSpinBox()
        self.translate_minY.setRange(0, 500)

        self.translate_minZ = QSpinBox()
        self.translate_minZ.setRange(0, 500)

        self.translate_maxX = QSpinBox()
        self.translate_maxX.setRange(0, 500)

        self.translate_maxY = QSpinBox()
        self.translate_maxY.setRange(0, 500)

        self.translate_maxZ = QSpinBox()
        self.translate_maxZ.setRange(0, 500)

        translate_layout.addWidget(QLabel("min x :"), 0, 0)
        translate_layout.addWidget(self.translate_minX, 0, 1)
        translate_layout.addWidget(QLabel("min y :"), 0, 2)
        translate_layout.addWidget(self.translate_minY, 0, 3)
        translate_layout.addWidget(QLabel("min z :"), 0, 4)
        translate_layout.addWidget(self.translate_minZ, 0, 5)

        translate_layout.addWidget(QLabel("max x :"), 1, 0)
        translate_layout.addWidget(self.translate_maxX, 1, 1)
        translate_layout.addWidget(QLabel("max y :"), 1, 2)
        translate_layout.addWidget(self.translate_maxY, 1, 3)
        translate_layout.addWidget(QLabel("max z :"), 1, 4)
        translate_layout.addWidget(self.translate_maxZ, 1, 5)

        self.layout.addWidget(translate)


    def rotate_parameters(self):
        rotate = QGroupBox("Rotate Parameters")
        rotate_layout = QGridLayout(rotate)

        self.rotate_minX = QSpinBox()
        self.rotate_minX.setRange(0, 500)

        self.rotate_minY = QSpinBox()
        self.rotate_minY.setRange(0, 500)

        self.rotate_minZ = QSpinBox()
        self.rotate_minZ.setRange(0, 500)

        self.rotate_maxX = QSpinBox()
        self.rotate_maxX.setRange(0, 500)

        self.rotate_maxY = QSpinBox()
        self.rotate_maxY.setRange(0, 500)

        self.rotate_maxZ = QSpinBox()
        self.rotate_maxZ.setRange(0, 500)

        rotate_layout.addWidget(QLabel("min x :"), 0, 0)
        rotate_layout.addWidget(self.rotate_minX, 0, 1)
        rotate_layout.addWidget(QLabel("min y :"), 0, 2)
        rotate_layout.addWidget(self.rotate_minY, 0, 3)
        rotate_layout.addWidget(QLabel("min z :"), 0, 4)
        rotate_layout.addWidget(self.rotate_minZ, 0, 5)

        rotate_layout.addWidget(QLabel("max x :"), 1, 0)
        rotate_layout.addWidget(self.rotate_maxX, 1, 1)
        rotate_layout.addWidget(QLabel("max y :"), 1, 2)
        rotate_layout.addWidget(self.rotate_maxY, 1, 3)
        rotate_layout.addWidget(QLabel("max z :"), 1, 4)
        rotate_layout.addWidget(self.rotate_maxZ, 1, 5)

        self.layout.addWidget(rotate)


    def scale_parameters(self):
        scale = QGroupBox("Scale Parameters")
        scale_layout = QGridLayout(scale)

        self.scale_minX = QSpinBox()
        self.scale_minX.setRange(0, 500)

        self.scale_minY = QSpinBox()
        self.scale_minY.setRange(0, 500)

        self.scale_minZ = QSpinBox()
        self.scale_minZ.setRange(0, 500)

        self.scale_maxX = QSpinBox()
        self.scale_maxX.setRange(0, 500)

        self.scale_maxY = QSpinBox()
        self.scale_maxY.setRange(0, 500)

        self.scale_maxZ = QSpinBox()
        self.scale_maxZ.setRange(0, 500)

        scale_layout.addWidget(QLabel("min x :"), 0, 0)
        scale_layout.addWidget(self.scale_minX, 0, 1)
        scale_layout.addWidget(QLabel("min y :"), 0, 2)
        scale_layout.addWidget(self.scale_minY, 0, 3)
        scale_layout.addWidget(QLabel("min z :"), 0, 4)
        scale_layout.addWidget(self.scale_minZ, 0, 5)

        scale_layout.addWidget(QLabel("max x :"), 1, 0)
        scale_layout.addWidget(self.scale_maxX, 1, 1)
        scale_layout.addWidget(QLabel("max y :"), 1, 2)
        scale_layout.addWidget(self.scale_maxY, 1, 3)
        scale_layout.addWidget(QLabel("max z :"), 1, 4)
        scale_layout.addWidget(self.scale_maxZ, 1, 5)

        self.layout.addWidget(scale)       


    def on_clicked(self):
        # Execute la fonction dans animator.py
        animator.create_animation(self)



