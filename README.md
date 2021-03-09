# Image to ASCII

Converts an image into ASCII art

## Installation and usage

- Clone this repository & install dependencies:

```bash
git clone https://github.com/michaeljgallagher/Image-to-ASCII && cd Image-to-ASCII
pip install -r requirements.txt
```

It is recommended to use a virtual environment before installing dependenices and running the script:

```bash
python3 -m venv env
source env/bin/activate
```

- Place image in same directory or subdirectory as `main.py`
- Run `main.py`:

```bash
python main.py image.jpg
```

Use `-o` to specify the name of the output file. Defaults to `output.txt`:

```bash
python main.py image.jpg -o ascii_output.txt
```

Use `-p` to specify the max dimension (in pixels) of the height or the width. The original aspect ratio is maintained. Defaults to `150px`:

```bash
python main.py image.jpg -p 100
```

Use `-i` to invert the output:

```bash
python main.py image.jpg -i
```

Use `-l` to use a 70-character ASCII greyscale ramp, as opposed to the default 10-character greyscale ramp:

```bash
python main.py image.jpg -l
```

## Arguments

```bash
usage: main.py [-h] [-i] [-l] [-o OUTPUT] [-p PIXELS] image

Convert image files into ASCII art

positional arguments:
  image                 Full name of image. Image must be contained inside the
                        same folder as this script.

optional arguments:
  -h, --help            show this help message and exit
  -i, --invert          Invert the output
  -l, --long            Use a 70 character mapping rather than a 10 character
                        mapping.
  -o OUTPUT, --output OUTPUT
                        Name of output file. Defaults to "output.txt".
  -p PIXELS, --pixels PIXELS
                        Specify the the max size in pixels that a side of the
                        image can be. The original aspect ratio is maintained.
                        Defaults to 150px
```
