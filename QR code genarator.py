import os
import qrcode



def generate_qr_code():
    os.system('cls')
    data = input("Enter the data for the QR code: ").strip()
    
    if not data:
        print("Error: Data cannot be empty!")
        return
    
    qr = qrcode.make(data)
    
    while True:
        file_name = input("Name your file (without extension): ").strip()
        if file_name:
            break
        print("Invalid filename. Please enter a valid name.")
    
    file_path = f"{file_name}.png"
    qr.save(file_path)
    print(f"QR code successfully saved as {file_path}")


generate_qr_code()

