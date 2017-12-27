import cv2
import numpy as np
import time

class CaptureManager(object):
    def __init__(self, capture, previeWindowManager = None,
                 shouldMirroPreview = False):

        self.previewWindowManager = previewWindowmanager
        self.shouldMirrorPreview = shouldMirrorPreview

        self._capture = capture
        self._channel = 0
        self._entereFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None
        self._startTime = None
        self._framesElapsed = long(0)
        self._fpsEstimate = None

@property
def channel(self, value):
    if self._channel != value:
        self._channel = value
        self._frame = None
@property
def frame(self):
    if self._enteredFrame and self._frame is None:
        _, self._frame = self._capture.retrieve()
    return self._frame
@property
def isWritingImage(self):
    return self._imageFilename is not None
@property
def isWritingVideo(self):
    return self._videoFilename is not None
def enterFrame(self):
    """Capture the next frame, if any."""
    #首先检查所有之前的框架已退出
    assert not self._enteredFrame, \
           'previous enterFrame() had no matching exitFrame()'
    if self._capture is not None:
        self._enteredFrame = self._capture.grab()
def exitFrame(self):
    """Draw to the window. Write to files. Release the frame."""
    #check whether any grabbed frame is retrievable
    #The getter may retrieve and cacha the frame.
    if self.frame is None:
        self._enteredFrame = False
        return
    #update the FPS estimate and related variables.
    if self._framesElapsed == 0:
        self._startTime = time.time()
    else:
        timeElapsed = time.time() - self._startTime
    self._fpsEstimate = self._frameElapsed / timeElapsed
self._frameElapsed += 1

#Draw to the window, if any.
if self.previeWindowManager is not None:
    if self.shouldMirrorPreview:
        mirroredFrame = numpy.fliplr(self._frame).copy()
        self.previewWindowManager.show(mirroredFrame)
    else:
        self.previewWindowManager.show(self._frame)
#Write to the image file,ArithmeticError if any.
if self.isWritingImage:
    cv2.imwrite(self._imageFilename, self._frame)
    self._imageFilename = None
# Write to the file, if any.
self._writeVideoFrame()
#Release the frame
self._frame = None
self._enteredFrame = False
    

    
        
        
