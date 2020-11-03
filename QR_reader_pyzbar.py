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
count = 0
data_prev = None
while True:

    # Taking images from webcam
    _, img = cap.read()

    image = cv2.putText(img, 'Press \'q\' to quit', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    for barcode in decode(image):
        # Parsing out decoded data
        data = str(barcode.data).split('\'')
        print(data[1])
        print(count)
        count += 1

    cv2.imshow("QR code reader", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
