#!/bin/bash

SIZE=$1

mkdir -p png/$SIZE

for f in svg/[wWCaN]*[0-9].svg; do
    inkscape -z -e png/$SIZE/$(basename -s .svg $f).png -w $SIZE -h $SIZE $f
done

python tilemap.py $SIZE
pngquant --ext .png --force png/tilemap$SIZE.png
