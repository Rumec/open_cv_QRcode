"""
First version, doesn't work so well - use QR_reader_pyzbar.py insted
"""
import cv2

# Initialize the webcam as the source of images
cap = cv2.VideoCapture(0)
# Initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
data_prev = None
while True:
    # Taking images from webcam
    _, img = cap.read()
    # Detects QRcode, sets BB and detects data in QR code
    data_new, bbox, _ = detector.detectAndDecode(img)
    image = cv2.putText(img, 'Press \'q\' to quit', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    # Checks if there is a QRCode in the image
    if bbox is not None:
        for i in range(len(bbox[0])):
            # Draws BB

            # For testing purposes - finding out how data is represented
            # print(bbox[0])
            # print(tuple(bbox[0][i]), tuple(bbox[0][(i + 1) % len(bbox)]))
            cv2.line(img, tuple(bbox[0][i]), tuple(bbox[0][(i + 1) % len(bbox[0])]), color=(255, 63, 111), thickness=2)
        # Avoiding duplicities in printing out encoded data
        if data_new and data_new != data_prev:
            print("Data encoded: ", data_new)
    if data_new:
        data_prev = data_new
    cv2.imshow("QR code reader", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
