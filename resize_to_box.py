"""
Resize to box

Usage:
  resize_to_box.py <width_to_height> <folder> [<size>]
"""

from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import os
import sys
import numpy as np

from docopt import docopt

def main(args):
    times_h = float(args["<width_to_height>"])
    resized_folder = args["<folder>"]
    final_size = args["<size>"]

    if resized_folder in (".", "..") or len(resized_folder) < 1 or not os.path.exists(resized_folder):
        print("Error in the chosen resized folder", file=sys.stderr)
        sys.exit(1)

    if final_size is not None:
        final_size = tuple(map(int, final_size.split("x")))

    maxp = 0

    for filename in os.listdir("."):
        if filename.lower().endswith(".jpg"):
            if os.path.exists(os.path.join(resized_folder, filename)):
                print("Skipping", filename, file=sys.stderr)
                continue

            im = Image.open(filename)
            w = im.width
            h = im.height
            old_num_px = h * w

            print("old size:", w, "x", h, file=sys.stderr)
            print("proportion: 1 to", w / h, file=sys.stderr)
            new_w = int(h * times_h)
            if new_w > w:
                print("Add black ink on the right", file=sys.stderr)
                w = int(round(new_w))
            elif new_w < w:
                print("Add black ink on bottom", file=sys.stderr)
                h = int(round(w / times_h))
            else:
                print("Nothing to do", file=sys.stderr)
            print("new size:", w, "x", h, file=sys.stderr)
            print("proportion: 1 to", w / h, file=sys.stderr)

            new_num_px = h * w
            perc = 100 - old_num_px / new_num_px * 100

            maxp = max(maxp, perc)

            # actual resizing operation
            new_im = Image.new('RGB', (w, h), (0, 0, 0))
            new_im.paste(im, (0, 0))

            if final_size is not None:
                new_im = new_im.resize(final_size)

            new_im.save(os.path.join(resized_folder, filename))

            print("percentage of black in new pic:", perc, "%", file=sys.stderr)
            print("=====", file=sys.stderr)

    print("Biggest percentage:", maxp, "%", file=sys.stderr)

if __name__ == "__main__":
    args = docopt(__doc__, argv=None, help=True, version=None, options_first=False)
    main(args)