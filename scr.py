#!/usr/bin/env python3

import argparse

# import the required library
import cv2
import drawsvg as draw

# define a function to display the coordinates of
# of the points clicked on the image

POINTS = []


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(f'({x},{y})')
        POINTS.append((x, y))
        # put coordinates as text on the image
        cv2.putText(
            img, f"({x},{y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
        )

        # draw point on the image
        cv2.circle(img, (x, y), 3, (0, 255, 255), -1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="caligram_express",
        description="Make a caligram given a text and an image.",
    )
    parser.add_argument(
        "IMAGE",
        type=argparse.FileType("r"),
        help="Path of the image that you want to use.",
    )
    parser.add_argument(
        "TEXT",
        type=argparse.FileType("r"),
        help="Path of the text file you want to use",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="example",
        help="Save output x in 'x.svg' and 'x.png'",
    )
    args = parser.parse_args()

    text = args.TEXT.read()
    text = text.replace("\n", " ")

    # read the input image
    img = cv2.imread(args.IMAGE.name)
    height = img.shape[0]
    width = img.shape[1]

    # create a window
    cv2.namedWindow("Point Coordinates")

    # bind the callback function to window
    cv2.setMouseCallback("Point Coordinates", click_event)

    # display the image
    while True:
        cv2.imshow("Point Coordinates", img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # echap
            break
    cv2.destroyAllWindows()

    d = draw.Drawing(width, height, origin=(0, 0), displayInline=False)
    p = draw.Path()
    POINTS = [(x, height - y) for x, y in POINTS]
    p.M(*POINTS.pop(0))
    for point in POINTS:
        p.L(*point)

    d.append(draw.Text(text, 30, path=p, text_anchor="start", valign="middle"))

    # d.append(p)
    d.save_svg(f"{args.output}.svg")
    d.save_png(f"{args.output}.png")
