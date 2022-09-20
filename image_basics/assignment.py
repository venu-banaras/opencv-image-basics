# can run only in script
import cv2
import numpy as np

# read the image
img = cv2.imread("dog_backpack.jpg")


def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 80, (255, 0, 0), 10)


cv2.namedWindow(winname="Dog")
cv2.setMouseCallback("Dog", draw_circle)

# open image in new window
while True:
    cv2.imshow("Dog", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
