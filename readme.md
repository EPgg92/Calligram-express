# Caligram express

Create Caligram quickly with highly inspired script from:

- <https://www.tutorialspoint.com/opencv-python-how-to-display-the-coordinates-of-points-clicked-on-an-image>
- <https://pypi.org/project/drawSvg/#basic-drawing-elements>

## Quick install

```sh
pipenv install
```

## Usage

```sh
./scr.py $IMAGE_PATH $TEXT_PATH -o caligram1 # create ./caligram1.png and ./caligram1.svg
```

```txt
usage: caligram_express [-h] [-o OUTPUT] IMAGE TEXT

Make a caligram given a text and an image.

positional arguments:
  IMAGE                 Path of the image that you want to use.
  TEXT                  Path of the text file you want to use

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Save output x in 'x.svg' and 'x.png'
```
