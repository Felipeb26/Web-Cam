import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened() == False:
    print("Error reading video file")
frame_width = int(webcam.get(3))
frame_height = int(webcam.get(4))

size = (frame_width, frame_height)
result = cv2.VideoWriter("teste1.avi", cv2.VideoWriter_fourcc(*"MJPG"), 10, size)

while True:
    ret, frame = webcam.read()

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()