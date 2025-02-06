import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 300)

while True:
    success, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier('feces.xml')

    results = faces.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=2)

    for (x, y, w, h) in results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

    cv2.imshow('result', img)
    cv2.waitKey(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break