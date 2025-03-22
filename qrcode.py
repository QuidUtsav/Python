#Installing the pyqrcode package by pip install pyqrcode
import pyqrcode

#getting the link or text from user
text =input("enter text to generate qr code: ")

#creating the pyqrcode object using create method with text as argument

qr_code = pyqrcode.create(text)

#saving the qr code in png format with name as qr_code.svg
qr_code.svg('qr_code.svg', scale = 8)