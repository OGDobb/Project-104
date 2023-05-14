import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (100, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))

cv2.putText(img, "Mercury", (125, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.putText(img, "Venus", (170, 200), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255))

cv2.putText(img, "Earth", (270, 270), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255))

cv2.putText(img, "Moon", (290, 150), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255))

cv2.putText(img, "Mars", (370, 170), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255))

cv2.putText(img, "Jupiter", (500, 200), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255))

cv2.putText(img, "Saturn", (700, 170), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255))

cv2.putText(img, "Uranus", (900, 150), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255))

cv2.putText(img, "Neptune", (1100, 150), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255))

cv2.imshow('Solar System', img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)


