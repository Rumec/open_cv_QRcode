"""
There is need to install zbar DLLs:

Linux: sudo apt-get install libzbar0
apple: brew install zbar

then install pyzbar library: pip3 install pyzbar
"""

import cv2
from pyzbar.pyzbar import decode

# Initialize the webcam as the source of images
cap = cv2.VideoCapture(0)
data_prev = None
while True:

    # Taking images from webcam
    _, img = cap.read()

    for barcode in decode(img):
        # Parsing out decoded data
        print(str(barcode.data)[1:])

        ####################################################################################
        # Following code is only for testing purposes, remove if you need better performance
        for i in range(len(barcode.polygon)):
            # Draws BB
            cv2.line(img, barcode.polygon[i], barcode.polygon[(i + 1) % len(barcode.polygon)], color=(255, 63, 111), thickness=2)
        image = cv2.putText(img, 'QR code detected!', (340, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                            cv2.LINE_AA)
        ####################################################################################

    image = cv2.putText(img, 'Press \'q\' to quit', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("QR code reader", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
