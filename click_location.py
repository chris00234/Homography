import numpy as np
import matplotlib.pyplot as plt
import cv2
import scipy

points = []


def click_event(event, x, y, flags, params): 

    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 

        # displaying the coordinates 
        # on the Shell 
        print(x, ' ', y)
        points.append((x,y))

        # displaying the coordinates 
        # on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font, 
                    5, (255, 0, 0), 2) 
        cv2.imshow('image', img)


img = cv2.imread('center.JPG', 1) 

# displaying the image 
cv2.imshow('image', img)   
# setting mouse handler for the image 
# and calling the click_event() function 
cv2.setMouseCallback('image', click_event) 

# wait for a key to be pressed to exit 
cv2.waitKey(0)   
# close the window 
cv2.destroyAllWindows()
with open('location.txt', "a") as f:
    f.write(str(points) + "\n")