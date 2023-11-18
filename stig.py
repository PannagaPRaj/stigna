import cv2
import os

img = cv2.imread('mypic.jpg')
msg = input("Enter secret message: ")
password = input("Enter password: ")
encryption_dict = {chr(i): i for i in range(256)}
decryption_dict = {i: chr(i) for i in range(256)}
index_n, index_z = 0, 0  
for char in msg:
    img[index_n, index_z, 0] = encryption_dict[char]
    index_n += 1
    index_z = (index_z + 1) % 3
cv2.imwrite("EncryptedMsg.jpg", img)
os.system("start EncryptedMsg.jpg")
decrypted_message = ""
index_n, index_z = 0, 0
entered_password = input("Enter passcode for Decryption: ")
if password == entered_password:
    for _ in range(len(msg)):
        pixel_value = int(img[index_n, index_z, 0])
        decrypted_message += decryption_dict[pixel_value]
        index_n += 1
        index_z = (index_z + 1) % 3
    print("Decryption message:", decrypted_message)
else:
    print("Not a valid key.")
