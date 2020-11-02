import qrcode
import numpy as np
import image
import random

data = input("Link:")
name = input("İsim:")

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make()
img = qr.make_image(fill_color="black", back_color="pink")
img.save(f"D:\Kodlama\pythonproje\qr\{name}.png")
img.show(f"D:\Kodlama\pythonproje\qr\{name}.png")