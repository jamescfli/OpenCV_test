import cv2

cv2.startWindowThread()
img = cv2.imread('images/eagle.jpg')
print img.__class__
cv2.namedWindow('opencv')
cv2.imshow('opencv', img)
cv2.waitKey(0)
cv2.destroyAllWindows()