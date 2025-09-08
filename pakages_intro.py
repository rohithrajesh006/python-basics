"""from gtts import gTTS
import os
s=input("Enter your text:")
c=gTTS(s)
c.save("test_audio.mp3")
os.system("start test audio.mp3")"""


import cv2 as cv
img=cv.imread("961dfafee629d47c9b7a7db70b1d893b.jpg")
cv.imshow("display window",img)
k=cv.waitKey(5000)