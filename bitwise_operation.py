import cv2
import numpy as np
img=np.zeros((250,500,3),np.uint8)
img=cv2.rectangle(img,(200,0),(300,100),(255,255,255),-1)
img1=cv2.imread(r'temp.png')
img1=cv2.resize(img1,(500,250))
cv2.imshow('img',img)
cv2.imshow('image',img1)
bit_and=cv2.bitwise_and(img1,img)
bit_or=cv2.bitwise_or(img1,img)
bit_xor=cv2.bitwise_xor(img1,img)
cv2.imshow('bitand',bit_and)
cv2.imshow('bitor',bit_or)
cv2.imshow('bitxor',bit_xor)
k=cv2.waitKey(0)
if k==ord('a'):
   cv2.destroyAllWindows()
