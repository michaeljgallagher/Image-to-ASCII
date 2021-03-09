from PIL import Image
import numpy as np
import argparse


# Greyscale character ramp from http://paulbourke.net/dataformats/asciiart/
PALETTE_LONG = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
PALETTE_SHORT = "@%#*+=-:. "


def resize_image(image, max_dimension):
    """
    Specify a maximum height or width to resize the image, while maintaing the aspect ratio.

    :type image: PIL.Image
    :type max_dimension: int
    :rtype: None
    """
    max_size = (max_dimension, max_dimension)
    return image.thumbnail(max_size, Image.ANTIALIAS)


def convert_to_ascii_matrix(image, palette):
    """
    Convert the greyscaled image into a matrix with ASCII characters.
    Specify the greyscale character ramp (palette)

    :type image: PIL.Image
    :type palette: str
    :rtype: List[List[str]]
    """
    matrix = np.asarray(image)  # Read image as matrix of pixel values

    rows, cols = len(matrix), len(matrix[0])
    res = [[None for _ in range(cols)] for _ in range(rows)]

    hi, lo = matrix.max(), matrix.min()
    variance = hi - lo

    for i, row in enumerate(matrix):
        for j, v in enumerate(row):
            # Scale values to corresponding palette character
            idx = ((v - lo) * (len(palette)-1)) // variance
            c = palette[idx]
            res[i][j] = c

    return res


def convert_to_string(matrix):
    """
    Convert the ascii matrix to a string for output

    :type matrix: List[List[str]]
    :rtype: str
    """
    res = []
    for row in matrix:
        res.append(''.join(row))
    return '\n'.join(res)


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description='Convert image files into ASCII art')
    parser.add_argument('image', type=str, action='store', default=None, help='Full name of image. Image\
        must be contained inside the same folder as this script.')
    parser.add_argument('-l', '--long', action='store_true', help='Use a 70 character mapping rather\
        than a 10 character mapping.')
    parser.add_argument('-o', '--output', type=str, action='store', default='output.txt', help='Name of output\
        file. Defaults to "output.txt".')
    parser.add_argument('-p', '--pixels', type=int, action='store', default=150, help='Specify the the max size\
        in pixels that a side of the image can be. The original aspect ratio is maintained. Defaults to 150px')
    args = parser.parse_args()

    palette = PALETTE_LONG if args.long else PALETTE_SHORT
    if not args.output.endswith('.txt'):
        args.output += '.txt'

    # Open image in context manager
    with Image.open(args.image) as img:
        # Scale-down original image:
        resize_image(img, args.pixels)

        # Convert to greyscale:
        img = img.convert(mode="L")

        # Convert to ascii_matrix
        matrix = convert_to_ascii_matrix(img, palette)

    # Convert to string for output
    out = convert_to_string(matrix)

    # Write to output file
    with open(args.output, 'w') as file:
        file.write(out)


if __name__ == '__main__':
    main()
