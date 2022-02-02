import cv2
detect = cv2.QRCodeDetector()
val,_,_ = detect.detectAndDecode(cv2.imread(input("Enter QRcode image name: ")))
print("Docoded value of QRcode : ",val)