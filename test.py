import qrcode

data = qrcode.make(input("Enter the data to for the QR code :"))

data.save("code.png")
