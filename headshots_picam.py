import cv2
# Import libraries for image processing (optional)
# import numpy as np

name = 'Moron'  # Replace with your name

# Define video capture object with device index (might need adjustment)
cap = cv2.VideoCapture(0)  # Change index if your camera has a different ID

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("Error: Unable to capture frame")
        break

    # Display captured frame
    cv2.imshow("Press Space to take a photo", frame)

    # Capture key press
    k = cv2.waitKey(1)

    # Handle key presses
    if k % 256 == 27:  # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:  # SPACE pressed
        img_name = "dataset/" + name + "/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
