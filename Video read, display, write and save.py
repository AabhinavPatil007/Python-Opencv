import cv2                                                                # import the library

cap = cv2.VideoCapture(0)                                                 # capture the video via 1st accessible camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')                                  # https://fourcc.org/codecs.php
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))              # record the video and save in .avi format

print(cap.isOpened())                                                     # To Check whether the Camera is working
while(cap.isOpened()):                                                    # While TRUE
    ret, frame = cap.read()                                               # 'ret' is boolean for True and False whether the camera/ video is working or not, repectively. frame for captruing the frames (Video).
    if ret == True:                                                       # IF 'ret' is TRUE
       print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))                           # To get the WIDTH of the FRAME and Print
       print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))                          # To get the HEIGHT of the FRAME and Print

       out.write(frame)                                                   # The Format in which the Video is being captured will get the data via frame (It's in BGR)

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                     # convert the colour of frames captured in frame from BGR to GRAY
       cv2.imshow('frame', gray)                                          # display the frames in GRAY

       if cv2.waitKey(1) & 0xFF == ord('q'):                              # IF 'q' pressed
         break                                                            # then, BREAK
    else:                                                                 # ELSE (of 1st used IF for ret == TRUE)
        break                                                             # If FALSE then BREAK

cap.release()                                                             # RELEASE THE CAMERA
out.release()                                                             # STOP CAPTURING THE FRAMES
cv2.destroyAllWindows()                                                   # DESTROY ALL THE WINDOWS

''' The Video is in BGR and the Live Display on the Screen is GRAY '''
