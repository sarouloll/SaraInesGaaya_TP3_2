from maya import cmds


def create_animation(self):
  # Appliquer sur les éléments séléctionnées
  selectionList = cmds.ls (selection=True, type='transform')

  #  Connection avec les valeurs entrées dans les spinbox
  duration = self.duration.value()
  step = self.step.value()

  # Définition de mes frames de début et de fin
  startFrame = int(cmds.playbackOptions(query=True, min=True))
  endFrame = startFrame + duration

  cmds.undoInfo(openChunk=True) # CTRL Z

  try:
      # fonctions à exécuter 
      translation_animation(self, selectionList, startFrame, endFrame)
      rotation_animation(self, selectionList, startFrame, endFrame)
      scale_animation(self, selectionList, startFrame, endFrame)

      # Mettre des steps à chaque nombre de frames définit sur la translation/rotation/scale
      cmds.bakeResults(selectionList, sampleBy = step, preserveOutsideKeys=True, sparseAnimCurveBake = False, 
                       attribute = [ 'translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 
                                    'rotateZ', 'scaleX', 'scaleY', 'scaleZ'])
  finally:
      cmds.undoInfo(closeChunk=True) # CTRL Z

  
def translation_animation(self, selectionList, startFrame, endFrame):

  for object in selectionList:
    cmds.setKeyframe(object, time=startFrame, attribute='translateX', value=self.translate_minX.value())
    cmds.setKeyframe(object, time=startFrame, attribute='translateY', value=self.translate_minY.value())
    cmds.setKeyframe(object, time=startFrame, attribute='translateZ', value=self.translate_minZ.value())

    cmds.setKeyframe(object, time=endFrame, attribute='translateX', value=self.translate_maxX.value())
    cmds.setKeyframe(object, time=endFrame, attribute='translateY', value=self.translate_maxY.value())
    cmds.setKeyframe(object, time=endFrame, attribute='translateZ', value=self.translate_maxZ.value())
      

def rotation_animation(self, selectionList, startFrame, endFrame):

  for object in selectionList:
    cmds.setKeyframe(object, time=startFrame, attribute='rotateX', value=self.rotate_minX.value())
    cmds.setKeyframe(object, time=startFrame, attribute='rotateY', value=self.rotate_minY.value())
    cmds.setKeyframe(object, time=startFrame, attribute='rotateZ', value=self.rotate_minZ.value())

    cmds.setKeyframe(object, time=endFrame, attribute='rotateX', value=self.rotate_maxX.value())
    cmds.setKeyframe(object, time=endFrame, attribute='rotateY', value=self.rotate_maxY.value())
    cmds.setKeyframe(object, time=endFrame, attribute='rotateZ', value=self.rotate_maxZ.value())


def scale_animation(self, selectionList, startFrame, endFrame):

  for object in selectionList:
    cmds.setKeyframe(object, time=startFrame, attribute='scaleX', value=self.scale_minX.value())
    cmds.setKeyframe(object, time=startFrame, attribute='scaleY', value=self.scale_minY.value())
    cmds.setKeyframe(object, time=startFrame, attribute='scaleZ', value=self.scale_minZ.value())

    cmds.setKeyframe(object, time=endFrame, attribute='scaleX', value=self.scale_maxX.value())
    cmds.setKeyframe(object, time=endFrame, attribute='scaleY', value=self.scale_maxY.value())
    cmds.setKeyframe(object, time=endFrame, attribute='scaleZ', value=self.scale_maxZ.value())

