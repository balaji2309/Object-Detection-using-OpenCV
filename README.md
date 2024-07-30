# Object-Detection-using-OpenCV
This project uses OpenCV for real-time motion detection via a webcam and sends an SMS alert through Twilio when movement is detected. It's ideal for basic security monitoring or surveillance applications.

# Detailed Steps
Initialization:

Import necessary libraries: cv2 (OpenCV), numpy, and twilio.rest.Client.
Initialize the Twilio client with account_sid and auth_token from a keys module.
Video Capture:

Start capturing video from the webcam using cv2.VideoCapture(0).
Read two consecutive frames (frame1 and frame2) to compare for motion detection.
Motion Detection Loop:

Calculate the absolute difference between the two frames to highlight changes.
Convert the difference image to grayscale, apply Gaussian blur, and threshold to create a binary image.
Dilate the binary image to enhance features and find contours in the image.
Contour Processing:

Iterate through the detected contours. For each contour, calculate its bounding rectangle.
If the contour area is large enough (greater than 900 pixels), draw a rectangle around the detected movement and add a "Movement" status text on the frame.
If movement is detected and no previous notification has been sent (movement_detected flag), send an SMS using Twilio and set the flag to avoid repeated messages.
Display and Frame Update:

Show the processed frame with detected movement in a window.
Update frame1 and frame2 for the next iteration.
Check for an ESC key press (cv2.waitKey(1) == 27) to exit the loop.
Cleanup:

Release the video capture and destroy all OpenCV windows when the loop ends.
