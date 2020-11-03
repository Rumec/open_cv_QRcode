"""
There is need to install zbar DLLs:

Linux: sudo apt-get install libzbar0
Apple: brew install zbar
Windows: Windows has it by default

then install pyzbar library: pip3 install pyzbar
"""

import cv2
import time
from pyzbar.pyzbar import decode

# Initialize the webcam as the source of images
cap = cv2.VideoCapture(0)

while True:
    # Timestamp in ms
    start = int(round(time.time() * 1000))
    # Taking images from webcam
    _, img = cap.read()

    for barcode in decode(img):
        # Parsing out decoded data
        print(str(barcode.data)[1:].strip('\''))

        ####################################################################################
        # Following code is only for testing purposes, remove if you need better performance
        for i in range(len(barcode.polygon)):
            # Draws BB
            cv2.line(img, barcode.polygon[i], barcode.polygon[(i + 1) % len(barcode.polygon)], color=(255, 63, 111),
                     thickness=2)
        image = cv2.putText(img, 'QR code detected!', (340, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                            cv2.LINE_AA)
        ####################################################################################

    cv2.putText(img, 'Press \'q\' to quit', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    end = int(round(time.time() * 1000))

    cv2.rectangle(img, (460, 440), (640, 480), (0, 0, 0),  - 1)
    cv2.putText(img, "FPS: " + str(1000 / (end - start)), (465, 470), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                cv2.LINE_AA)
    cv2.imshow("QR code reader", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
