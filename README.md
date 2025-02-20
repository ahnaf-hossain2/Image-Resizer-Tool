# Image-Resizer-Tool
This tool will resize your image while maintaining its aspect ratio. But also you can do it without maintaining the aspect ratio. This is
A Python script to resize images to specific dimensions or while maintaining the original aspect ratio. Built using the Pillow library.

## Features

1. **Resize to Exact Dimensions**: Resize an image to exact width and height (may distort the image if the aspect ratio differs).
2. **Maintain Aspect Ratio**: Resize an image by specifying either width or height, and automatically calculate the other dimension to preserve the aspect ratio.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. **Clone the repository**:
   ```bash
   git clone "https://github.com/ahnaf-hossain2/Image-Resizer-Tool.git"
   cd image-resizer-python

2. Install Pillow:
   ```bash
   pip install Pillow

## Usage

1. resize_image.py (Exact Dimensions)
First open the cmd. Then goto your file location(for example):

   ```bash
   "C:\Users\User\Desktop\GitHub\Image resizer python"


   ```bash


Resize an image to specific dimensions (width and height).
   ```bash
   python resize_image.py <input_path> <output_path> <width> <height>
