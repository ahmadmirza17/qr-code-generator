import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

qr.add_data(input("Enter website:"))
qr.make(fit=True)

img = qr.make_image(fill_color="orange", back_color="black")
img.save("advanced.png")
