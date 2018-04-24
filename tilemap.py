import sys
import os.path as op
from glob import glob
from PIL import Image

W = int(sys.argv[1])
ROWS = ['ww' + str(i) for i in range(10)] + ['W', 'a', 'CL', 'CM', 'CH', 'N']
TILEMAP = Image.new('RGBA', size=(10*W, len(ROWS)*W), color=(255, 255, 255, 0))

for row in range(len(ROWS)):
    im_str = ROWS[row]
    for col in range(10):
        im_name = op.join('png', str(W), im_str + str(col) + '.png')
        if not op.exists(im_name):
            continue
        im = Image.open(im_name)
        TILEMAP.paste(im, (col*W, row*W))

TILEMAP.save(op.join('png', 'tilemap' + str(W) + '.png'))
