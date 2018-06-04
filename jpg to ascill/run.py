

# coding: utf8
import os
from PIL import Image
img = Image.open("input.jpg")
print("Size of image:")
print (img.size)

x,y = img.size
font = input("if you use a monospaced font,please tap 1,else 2:")
if font == 1:
    font = 1
elif font == 2:
    font = 2
else:
    font = 2
a = input ("a:")
b = str(int((y/(font*x))*float(a)))
run = 'python .\\ascii.py .\\input.jpg -o output.txt --width '+a+' --height ' + b
os.system(run)
os.system("output.txt")
