# /usr/bin/env python
# coding=utf-8


from PIL import Image, ImageFilter


im = Image.open('/Users/nana/Downloads/test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('/Users/nana/Downloads/test.jpg', 'jpeg')
