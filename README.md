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

First open the cmd. Then goto your file location(for example):
   ```bash
   "C:\Users\User\Desktop\GitHub\Image resizer python"

1. resize_image.py (Exact Dimensions)
Resize an image to specific dimensions (width and height).
  ```bash
  python resize_image.py <input_path> <output_path> <width> <height>

Example:
    ```bash
    python resize_with_aspect_ratio.py input.jpg output.jpg --width 800

2. resize_with_aspect_ratio.py (Maintain Aspect Ratio)
Resize an image while preserving the aspect ratio. Specify either --width or --height.

    ```bash
    python resize_with_aspect_ratio.py <input_path> <output_path> --width <target_width> --height <target_height>
Examples:
Resize based on width:
    ```bash
    python resize_with_aspect_ratio.py input.jpg output.jpg --width 800

Resize based on height:
    ```bash
    python resize_with_aspect_ratio.py input.jpg output.jpg --height 600

## How It Works

resize_image.py
* Uses Pillow's Image.resize() method with LANCZOS resampling for high-quality output.
* Accepts exact width and height as arguments.

resize_with_aspect_ratio.py
* Automatically calculates missing dimensions to preserve the original aspect ratio.
* Flexible: Specify either width or height (or both for exact resizing).

Command-Line Arguments
For resize_image.py:
Argument	Description
input_path	Path to the input image
output_path	Path to save the resized image
width	Target width in pixels (integer)
height	Target height in pixels (integer)
For resize_with_aspect_ratio.py:
Argument	Description
input_path	Path to the input image
output_path	Path to save the resized image
--width	Target width (optional)
--height	Target height (optional)

## Example Output:

Original Image(1920x1080)
Resized to 800x600
Resized with Aspect Ratio(width=800)

Contributing
Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

License
This project is licensed under the MIT License. See LICENSE for details.
