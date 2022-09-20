# in this we are learning to open image files using opencv and python script i.e. using .py files.
# here we simply open a file using opencv in a separate window

import cv2

img = cv2.imread(
    "D:/Computer vision learning/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg"
)

# below we are giving condition for when window will close
# when true means when the window is open, because of imshow() function we go to the if condition
# then inside the if we are checking that have we pressed the ESC key? and if we waited atlest 1ms then close the window . this line is the same comment
#  inside the while loop. there is also a stackoverflow link in the course. which gives detailed explanation
while True:
    cv2.imshow("Doggy", img)
    # if we wait atleast 1 millisecond AND we pressed Esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# we can close the window by pressing esc key.
cv2.destroyAllWindows()

# we first write code in jupyter. but since we want to open images in separate window we will have to use .py files
# . so we first write code in jupyter and then copy it into .py file we need.
