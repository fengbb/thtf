from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import pytesseract
image = Image.open('D:\\pycharmproject\\untitled1\\1.gif')
vcode = pytesseract.image_to_string(image)
print (vcode)
