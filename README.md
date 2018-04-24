# synop\_tilemap

![SYNOP Tilemap](png/tilemap24.png)

Assets for creating tilemap with synoptic symbols used in SYNOP code.

SVG files from [WikiMedia](https://commons.wikimedia.org/wiki/Weather_map).

Generated tilemap is used for [drawing SYNOPs on HTML canvas](https://github.com/alexander-travov/synop_canvas).

## Requirements:

* Inkscape for SVG-PNG conversion
* PIL for creating tilemap with python
* pngquant for optimizing output

```sh
apt install python-pil inkscape pngquant
```

## Usage:

Create 36px SYNOP tilemap. Output: `png/tilemap36.png`

```sh
./tilemap.sh 36
```
