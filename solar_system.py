import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(img,'Sol',(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255))

cv2.putText(img,'Mercurio',(125,185),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,'Venus',(200,175),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,'Terra',(295,170),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,'Marte',(385,175),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,'Jupiter',(560,55),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Saturno',(835,160),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,'Urano',(980,140),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,'Netuno',(1125,145),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))

cv2.imshow('resultado',img)
cv2.waitKey(0)
#cv2.imwrite(“Solar_systemwithname.jpg”,img)