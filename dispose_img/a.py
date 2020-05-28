import sys
sys.path.append("./dispose_img")

from PIL import Image

img = Image.open('./a.jpg')
img_size = img.size
w = img_size[0]
h = img_size[1]
reg = img.crop((0, 0, w, 160))
reg.save('top.jpg')

reg = img.crop((0, 160, 84, h))
reg.save('foot.jpg')