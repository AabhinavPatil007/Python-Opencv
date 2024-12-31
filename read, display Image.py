import cv2
print(cv2.__version__)

'''
Read an image

cv2.imread() Second argument is a flag which specifies the way image should be read.

       flag	            integer value	         description
cv2.IMREAD_COLOR	        1	           Loads a color image.
cv2.IMREAD_GRAYSCALE	    0	           Loads image in grayscale mode
cv2.IMREAD_UNCHANGED	   -1	           Loads image as such including alpha channel

'''

img = cv2.imread('lena.jpg', -1)                   # Even if we enter wrong file name then, also NO ERROR IS SHOWCASED
print(img)                                        # ONLY YOU WON'T GET AN OUTPUT

cv2.imshow('image', img)                 # To Display the Image
k = cv2.waitKey(0) # & 0xFF       Optional (use incase it doesn't work

if k == 27:                                       # IF 'esc' is pressed
  cv2.destroyAllWindows()                         # then all windows including the displayed image window is destroyed

elif k == ord('s'):                               # ELIF 's' is pressed
  cv2.imwrite('lena_copy.png', img)       # then a copy of the 'lena.jpg' is saved as 'lena_copy.png'
  cv2.destroyAllWindows()                         # finally all windows including the displayed image window is destroyed

  