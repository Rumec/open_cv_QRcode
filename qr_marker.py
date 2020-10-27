import cv2

# Initialize the webcam as the source of images
cap = cv2.VideoCapture(0)
# Initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    # Taking images from webcam
    _, img = cap.read()
    # Detects QRcode, sets BB and detects data in QR code
    data, bbox, _ = detector.detectAndDecode(img)

    # Checks if there is a QRCode in the image
    if bbox is not None:
        for i in range(len(bbox)):
            # Draws BB
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
        if data:
            print("Data encoded: ", data)

    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()
