# Calligram express

Create Calligram quickly with highly inspired script from:

- <https://www.tutorialspoint.com/opencv-python-how-to-display-the-coordinates-of-points-clicked-on-an-image>
- <https://pypi.org/project/drawSvg/#basic-drawing-elements>

## Quick install

Install poetry <https://python-poetry.org/docs/#installation>

```sh
poetry install
```

## Usage

```sh
poetry shell # lauch the env to use poetry env dependency

poetry run ./calligram_express/scr.py $IMAGE_PATH $TEXT_PATH -o calligram1 # create ./calligram1.png and ./calligram1.svg
```

```txt
usage: calligram_express [-h] [-o OUTPUT] IMAGE TEXT

Make a calligram given a text and an image.

positional arguments:
  IMAGE                 Path of the image that you want to use.
  TEXT                  Path of the text file you want to use

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Save output x in 'x.svg' and 'x.png'
```
