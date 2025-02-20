from PIL import Image
import argparse

def resize_image(input_path, output_path, width=None, height=None):
    try:
        with Image.open(input_path) as img:
            # Calculate dimensions to maintain aspect ratio
            original_width, original_height = img.size
            if width and height:
                # Resize to exact dimensions (may distort the image)
                new_size = (width, height)
            elif width:
                # Resize based on width, maintaining aspect ratio
                ratio = width / original_width
                new_size = (width, int(original_height * ratio))
            elif height:
                # Resize based on height, maintaining aspect ratio
                ratio = height / original_height
                new_size = (int(original_width * ratio), height)
            else:
                raise ValueError("Either width or height must be provided")

            resized_img = img.resize(new_size, resample=Image.LANCZOS)
            resized_img.save(output_path)
            print(f"Image resized and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize an image while maintaining aspect ratio.")
    parser.add_argument("input", help="Path to the input image")
    parser.add_argument("output", help="Path to save the resized image")
    parser.add_argument("--width", type=int, help="Desired width in pixels (optional)")
    parser.add_argument("--height", type=int, help="Desired height in pixels (optional)")

    args = parser.parse_args()
    resize_image(args.input, args.output, args.width, args.height)
