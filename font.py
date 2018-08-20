from PIL import Image
from uuid import uuid1
import pytesseract
import os
# im = ImageGrab.grab()
# Image.DEBUG
# im.save(uuid4() + ".jpg")
im = Image.open(os.getcwd() + "/1.jpg")
# print()
text = pytesseract.image_to_string(im,lang="chi_sim")
print(text)