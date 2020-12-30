from cv2 import cv2  

src = cv2.imread('pending.png')
window_name ='image'
image = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
cv2.imshow(window_name,image)
