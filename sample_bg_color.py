from PIL import Image, ImageSequence
import sys
p = 'bg.gif'
try:
    im = Image.open(p)
except Exception as e:
    print('ERROR_OPEN', e)
    sys.exit(2)

total = [0,0,0]
count = 0
for frame in ImageSequence.Iterator(im):
    rgba = frame.convert('RGBA')
    w,h = rgba.size
    pixels = rgba.load()
    for y in range(h):
        for x in range(w):
            r,g,b,a = pixels[x,y]
            if a == 0:
                continue
            total[0] += r
            total[1] += g
            total[2] += b
            count += 1

if count == 0:
    print('NO_PIXELS')
    sys.exit(3)

avg = tuple(int(total[i]/count) for i in range(3))
hexc = '#{:02x}{:02x}{:02x}'.format(*avg)
print(hexc)
print(avg)
