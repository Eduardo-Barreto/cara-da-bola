import cv2

ANNOTATE_EYES = True 

face_cascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("cascades/haarcascade_eye.xml")

video_path = "./la_cabra.mp4"
cap = cv2.VideoCapture(video_path)
success, frame = cap.read()

height, width, layers = frame.shape
annotated_video = cv2.VideoWriter("final.avi", 0, 30, (width, height))

while cap.isOpened() and success:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for x, y, w, h in faces:
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15)
        )

        if len(eyes) < 1:
            continue

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if not ANNOTATE_EYES:
            continue

        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    annotated_video.write(frame)

    cv2.imshow("Video", frame)
    cv2.waitKey(1)
    success, frame = cap.read()

cap.release()
annotated_video.release()
cv2.destroyAllWindows()
