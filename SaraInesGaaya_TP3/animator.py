from maya import cmds
import ui


def create_animation(duration):
  
  selectionList = cmds.ls (selection=True, type='transform')
  cmds.undoInfo(openChunk=True) # CTRL Z

  #endFrame = cmds.playbackOptions(query=True, maxTime=True)
  #duration = self.duration_spin.value()
  #value = 0

  #cmds.setKeyframe(selectionList, time=endFrame, value=value)


 ##end frame = duration de ui.py
   # startFrame = cmds.playbackOptions(query=True, minTime=True)
   # endFrame = cmds.playbackOptions(query=True, maxTime=True)

  
def translation_animation(self):
  selectionList = cmds.ls (selection=True, type='transform')
  startFrame = 0
    
  for object in selectionList:
    cmds.setKeyframe(selectionList, time=startFrame, attribute='translateX', value=self.translate_minX.value() )
    cmds.setKeyframe(selectionList, time=startFrame, attribute='translateY', value=self.translate_minY.value() )
    cmds.setKeyframe(selectionList, time=startFrame, attribute='translateZ', value=self.translate_minZ.value() )


def rotation_animation(self):
  selectionList = cmds.ls (selection=True, type='transform')
  startFrame = 0

  for object in selectionList:
    cmds.setKeyframe(selectionList, time=startFrame, attribute='rotateX', value=self.rotate_minX.value() )
    cmds.setKeyframe(selectionList, time=startFrame, attribute='rotateY', value=self.rotate_minY.value() )
    cmds.setKeyframe(selectionList, time=startFrame, attribute='rotateZ', value=self.rotate_minZ.value() )


def scale_animation(self):
  selectionList = cmds.ls (selection=True, type='transform')
  startFrame = 0

  for object in selectionList:
    cmds.setKeyframe(selectionList, time=startFrame, attribute='scaleX', value=self.scale_minX.value() )
    cmds.setKeyframe(selectionList, time=startFrame, attribute='scaleY', value=self.scale_minY.value() )
    cmds.setKeyframe(selectionList, time=startFrame, attribute='scaleZ', value=self.scale_minZ.value() )





    



# selectionList = cmds.ls (selection=True, type='transform')

# startFrame = cmds.playbackOptions(query=True, minTime=True)
# endFrame = cmds.playbackOptions(query=True, maxTime=True)


# for pCube1 in selectionList:
#     cmds.setKeyframe(pCube1, time=startFrame, attribute='translateZ', value = 0 )
#     cmds.setKeyframe(pCube1, time=startFrame, attribute='translateX', value = 0 )

#     cmds.setKeyframe(pCube1, time=startFrame + 10, attribute='translateZ', value=25)
#     cmds.setKeyframe(pCube1, time=startFrame + 10, attribute='translateX', value=50)

#     cmds.setKeyframe(pCube1, time=startFrame + 40, attribute='translateZ', value=50)
#     cmds.setKeyframe(pCube1, time=startFrame + 60, attribute='translateX', value=75)
   
#     cmds.setKeyframe(pCube1, time=endFrame, attribute='translateZ', value = 100 )
#     cmds.setKeyframe(pCube1, time=endFrame, attribute='translateX', value = 0 )

  cmds.undoInfo(closeChunk=True) # CTRL Z
