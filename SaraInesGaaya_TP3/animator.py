from maya import cmds
import random


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
      # Fonctions à exécuter 
      translation_animation(self, selectionList, startFrame, endFrame)
      rotation_animation(self, selectionList, startFrame, endFrame)
      scale_animation(self, selectionList, startFrame, endFrame)

      attributes = [ 'translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY', 'scaleZ']

      for object in selectionList:
        
        cmds.keyTangent(object, inTangentType='spline', outTangentType='spline')
        cmds.playbackOptions(minTime=startFrame, maxTime=endFrame)

      # Mettre des steps à chaque nombre de frames définit sur la translation/rotation/scale
      #cmds.bakeResults(selectionList, sampleBy = step, preserveOutsideKeys=True, sparseAnimCurveBake = False, attribute = attributes)
      # Supprime les anciennes données quand les valeurs sont changées + bouton Create
      #cmds.cutKey(selectionList, time=(startFrame, endFrame), attribute=attributes, clear=True)

  finally:
      cmds.undoInfo(closeChunk=True) # CTRL Z

  
def translation_animation(self, selectionList, startFrame, endFrame):

  for frame in range(startFrame + self.step.value(), endFrame, self.step.value()):
    
    for object in selectionList:
      cmds.setKeyframe(object, time=frame, attribute='translateX', value=random.uniform(self.translate_minX.value(), self.translate_maxX.value()))
      cmds.setKeyframe(object, time=frame, attribute='translateY', value=random.uniform(self.translate_minY.value(), self.translate_maxY.value()))
      cmds.setKeyframe(object, time=frame, attribute='translateZ', value=random.uniform(self.translate_minZ.value(), self.translate_maxZ.value()))

    # cmds.setKeyframe(object, time=endFrame, attribute='translateX', value=self.translate_maxX.value())
    # cmds.setKeyframe(object, time=endFrame, attribute='translateY', value=self.translate_maxY.value())
    # cmds.setKeyframe(object, time=endFrame, attribute='translateZ', value=self.translate_maxZ.value())
      

def rotation_animation(self, selectionList, startFrame, endFrame):

  for frame in range(startFrame + self.step.value(), endFrame, self.step.value()):

    for object in selectionList:
      cmds.setKeyframe(object, time=frame, attribute='rotateX', value=random.uniform(self.rotate_minX.value(), self.rotate_maxX.value()))
      cmds.setKeyframe(object, time=frame, attribute='rotateY', value=random.uniform(self.rotate_minY.value(), self.rotate_maxY.value()))
      cmds.setKeyframe(object, time=frame, attribute='rotateZ', value=random.uniform(self.rotate_minZ.value(), self.rotate_maxZ.value()))

    # cmds.setKeyframe(object, time=endFrame, attribute='rotateX', value=self.rotate_maxX.value())
    # cmds.setKeyframe(object, time=endFrame, attribute='rotateY', value=self.rotate_maxY.value())
    # cmds.setKeyframe(object, time=endFrame, attribute='rotateZ', value=self.rotate_maxZ.value())


def scale_animation(self, selectionList, startFrame, endFrame):

  for frame in range(startFrame + self.step.value(), endFrame, self.step.value()):

    for object in selectionList:
      cmds.setKeyframe(object, time=frame, attribute='scaleX', value=random.uniform(self.scale_minX.value(), self.scale_maxX.value()))
      cmds.setKeyframe(object, time=frame, attribute='scaleY', value=random.uniform(self.scale_minY.value(), self.scale_maxY.value()))
      cmds.setKeyframe(object, time=frame, attribute='scaleZ', value=random.uniform(self.scale_minZ.value(), self.scale_maxZ.value()))

    # cmds.setKeyframe(object, time=endFrame, attribute='scaleX', value=self.scale_maxX.value())
    # cmds.setKeyframe(object, time=endFrame, attribute='scaleY', value=self.scale_maxY.value())
    # cmds.setKeyframe(object, time=endFrame, attribute='scaleZ', value=self.scale_maxZ.value())

### TO DO
# loop animation, boucle fluide
# update bouton create
# commentaires sur ui et animator
