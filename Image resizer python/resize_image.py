from PIL import Image
import argparse

def resize_image(input_path, output_path, width, height):
    try:
        with Image.open(input_path) as img:
            # Resize the image using LANCZOS resampling for high quality
            resized_img = img.resize((width, height), resample=Image.LANCZOS)
            resized_img.save(output_path)
            print(f"Image resized and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize an image to specified dimensions.")
    parser.add_argument("input", help="Path to the input image")
    parser.add_argument("output", help="Path to save the resized image")
    parser.add_argument("width", type=int, help="Desired width in pixels")
    parser.add_argument("height", type=int, help="Desired height in pixels")

    args = parser.parse_args()
    resize_image(args.input, args.output, args.width, args.height)
