from PIL import Image
import sys
p='bg.gif'
try:
    im=Image.open(p)
except Exception as e:
    print('ERROR',e); sys.exit(1)
frame = im.convert('RGBA')
small = frame.resize((1,1), resample=Image.BOX)
r,g,b,a = small.getpixel((0,0))
hexc = '#{:02x}{:02x}{:02x}'.format(r,g,b)
print(hexc)
print((r,g,b))
