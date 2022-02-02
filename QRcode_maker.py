import qrcode
data = input("Enter a text/link to create it's qrcode:\n")

if data != "":
    img = qrcode.make(data)
    img.save(input("QRcode save as [*.jpg](Recommended):\n"))
    input("QRcode generated successfully")
else:
    input("no data given!!")