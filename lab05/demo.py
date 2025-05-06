import cv2 as cv

img = cv.imread('apollo.jpg')

print(type(img))
print(img.shape)

cv.imwrite('apollo.png', img)
cv.imshow('a great image', img)
cv.waitKey()
cv.destroyAllWindows()
