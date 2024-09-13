import qrcode

data = qrcode.make(input("Enter the data to for the QR code :"))

file_name = input("Name your file: ")




data.save(f"{file_name}.png")
