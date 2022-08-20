import cv2

cam = cv2.VideoCapture(0)

ret, image = cam.read()

cv2.imwrite('/home/sisyphii/Pictures/tes09t.jpg', image)