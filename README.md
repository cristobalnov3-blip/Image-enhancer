# Image Enlarger

A simple Python script that enlarges an image by 2x using pixel-based HSL color variations.

## Overview

This project uses Pillow and Python’s `colorsys` module to read an image, with each pixel, and create a new image that is twice the size of the original.  
Instead of copying pixels directly, it 'hopefully' will create 4 different pizels of similar colors for each pixel and places them in a 2x2 block.

## Features

- Doubles the size of an image.
- Uses HSL adjustments to create similar color variants.
- Saves the result as `output.png`.
- Works with any image format supported by Pillow.

## Requirements

- Python 3.x
- Pillow


## Usage

Run the script and enter the full path to your image when prompted:

You have to put your image in the same folder as the code for it to work

Example input:

```text
Enter the full path to your image: C:\Users\YourName\Pictures\photo.png
```

The script will create an enlarged version of the image in the same folder as the original and save it as:

```text
output.png
```

## How It Works

For each pixel in the original image, the script:

1. Converts the RGB color to HSL.
2. Creates four similar color pixels.
3. Writes those variants into a 2x2 block in the new image.
4. Saves the final image.


- The script uses `input()`, so it must be run in an interactive terminal.
- The `new_img.show()` call may not work in all environments.
- If you want a true upscale, you may want to use Pillow’s resize methods instead.

## License
