# 🖼️ Image-Resizer-Tool

A simple yet powerful Python utility for resizing images with flexibility. Resize images to exact dimensions or maintain aspect ratio using the high-quality Pillow library.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-green.svg)](https://www.python.org/)

## ✨ Features

- **Exact Dimension Resizing**: Set precise width and height values
- **Aspect Ratio Preservation**: Specify only width or height to maintain proportions
- **High-Quality Output**: Uses Lanczos resampling for superior results
- **Simple Command-Line Interface**: Easy to use with straightforward commands

## 🔧 Requirements

- Python 3.x
- Pillow library

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ahnaf-hossain2/Image-Resizer-Tool.git
   cd Image-Resizer-Tool
   ```

2. **Install Pillow**:
   ```bash
   pip install Pillow
   ```

## 📝 Usage

Navigate to the project directory:
```bash
cd path/to/Image-Resizer-Tool
```

### Method 1: Resize to Exact Dimensions
```bash
python resize_image.py <input_path> <output_path> <width> <height>
```

**Example**:
```bash
python resize_image.py input.jpg resized_output.jpg 800 600
```

### Method 2: Resize with Aspect Ratio Preservation
```bash
python resize_with_aspect_ratio.py <input_path> <output_path> [--width <width>] [--height <height>]
```

**Examples**:
- Resize based on width (height calculated automatically):
  ```bash
  python resize_with_aspect_ratio.py input.jpg resized_output.jpg --width 800
  ```

- Resize based on height (width calculated automatically):
  ```bash
  python resize_with_aspect_ratio.py input.jpg resized_output.jpg --height 600
  ```

## 🔍 How It Works

### `resize_image.py`
- Resizes images to exact dimensions specified by the user
- Uses Pillow's `Image.resize()` method with `LANCZOS` resampling algorithm
- May alter the aspect ratio if target dimensions don't match the original ratio

### `resize_with_aspect_ratio.py`
- Intelligently preserves the original aspect ratio of the image
- Calculates the missing dimension based on the provided one
- Ensures images look natural without stretching or distortion

## 📋 Command-Line Arguments

### For `resize_image.py`:

| Argument | Description |
|----------|-------------|
| `input_path` | Path to the source image |
| `output_path` | Path where the resized image will be saved |
| `width` | Target width in pixels (integer) |
| `height` | Target height in pixels (integer) |

### For `resize_with_aspect_ratio.py`:

| Argument | Description |
|----------|-------------|
| `input_path` | Path to the source image |
| `output_path` | Path where the resized image will be saved |
| `--width` | Target width in pixels (optional) |
| `--height` | Target height in pixels (optional) |

## 📊 Example Results

| Image | Dimensions | Description |
|-------|------------|-------------|
| Original | 1920×1080 | Source image |
| Exact Resize | 800×600 | Fixed dimensions (may alter aspect ratio) |
| Aspect Ratio Preserved | 800×450 | Width set to 800, height calculated automatically |

## 👨‍💻 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- GitHub Repository: [https://github.com/ahnaf-hossain2/Image-Resizer-Tool](https://github.com/ahnaf-hossain2/Image-Resizer-Tool)
- Report Issues: [https://github.com/ahnaf-hossain2/Image-Resizer-Tool/issues](https://github.com/ahnaf-hossain2/Image-Resizer-Tool/issues)
