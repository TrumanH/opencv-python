import cv2
'''
videoCapture = cv2.VideoCapture('00.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'),
    fps, size) #I420:一个未压缩的YUV颜色编码，4：2：0色度子采样.扩展名.avi
success, frame = videoCapture.read()
while success: #循环直至用完框架
    videoWriter.write(frame)
    success, frame = videoCapture.read() '''

#摄像头捕捉
cameraCapture = cv2.VideoCapture(0)
#fps = cameraCapture.get(cv2.CAP_PROP_FPS)
fps = 30 #一个假设值
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'),
    fps, size)
success, frame = cameraCapture.read()
num = 3*fps - 1
while success and num > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    num -= 1
cameraCapture.release()

#实时显示摄像头帧
clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('Mywindow')
cv2.setMouseCallback('Mywindow', onMouse)

print('Showing camera feed, Clickwindow or press any key to stop.')
success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('Mywindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('Mywindow')
cameraCapture.release()
