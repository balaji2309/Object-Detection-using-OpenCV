import cv2
import numpy as np
from twilio.rest import Client
import keys

# Initialize Twilio client
client = Client(keys.account_sid, keys.auth_token)

cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

movement_detected = False

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: Movement", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        
        if not movement_detected:
            message = client.messages.create(
                body="Movement of object detected",
                from_=keys.twilio_number,
                to=keys.phone_number
            )
            print(message.body)
            movement_detected = True  # Set flag to avoid repeated messages

    if not ret:
        break
    
    cv2.imshow("img", frame1)
    
    frame1 = frame2
    ret, frame2 = cap.read()
    
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
