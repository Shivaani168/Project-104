import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(100,400),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255))
cv2.putText(img,"Mercury",(120,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Venus",(190,175),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Earth",(290,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Mars",(380,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Jupiter",(580,380),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Saturn",(790,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Uranus",(970,290),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Neptune",(1110,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.imshow("Solar_systemwithname.jpg",img)
cv2.waitKey(0)