# To use this, you need to execute following command (for installing the library needed)
# pip3 install qrcode[pil]

import qrcode


def generate_qr(data, filename):
    # Data to be encoded to QR code
    data = data
    # Generating QR code
    img = qrcode.make(data)
    img.save(filename)

data_to_be_encoded = input("Enter the data: ")
filename = input("Enter name of the file: ")
generate_qr(data_to_be_encoded, filename)
