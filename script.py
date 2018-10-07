
# coding: utf-8

# In[2]:


import cv2
import numpy as np


# In[15]:


cap = cv2.VideoCapture(0)

while True:
    # Get capture
    ret, frame = cap.read()
    
    # Show capture
    cv2.imshow('frame', frame)
    
    # If pressed 'space' -> save image and stop capturing
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.imwrite('foto.jpeg', frame)
        break

# Release capture and destroy windows
cap.release()
cv2.destroyAllWindows()        


# In[ ]:


# Read image from disk in grayscale
img = cv2.imread('foto.jpeg', cv2.IMREAD_GRAYSCALE)

# Define image shape
img_width, img_height = img.shape

# Define color of the line and reacntangle
line_color = tuple(np.random.random(3) * 255)
rectangle_color = tuple(np.random.random(3) * 255)

# Define height and width of rectangle
rectangle_height = np.random.randint(0, 255)
rectangle_width = np.random.randint(0, 255)

# Defint coordinates of the corners of rectangle
rectangle_start = ((img_height - rectangle_height) // 2, (img_width - rectangle_width) // 2)
rectangle_end = (rectangle_start[0] + rectangle_height, rectangle_start[1] + rectangle_width)

#cv2.namedWindow('foto', cv2.WINDOW_NORMAL)
cv2.imshow('foto', img)
img = cv2.line(img, (0, 0), (img_height, img_width), line_color, 5)
img = cv2.rectangle(img, rectangle_start, rectangle_end, rectangle_color, 5)
cv2.imshow('foto', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


img_height


# In[10]:


type((1, 2, 3))

