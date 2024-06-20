from PIL import Image, ImageSequence
import sys
import time

# ASCII characters used for grayscale conversion (from darkest to lightest)
ASCII_CHARS = "@#S%?*+;:,."

def image_to_ascii(image, width=None):
    if width is None:
        # Set default width to maintain aspect ratio
        width = 100
    # Calculate height based on aspect ratio
    height = int((image.height / image.width) * width)
    # Resize image to desired dimensions
    image = image.resize((width, height))
    # Convert image to grayscale
    grayscale_image = image.convert("L")
    # Convert each pixel to ASCII character based on intensity
    ascii_str = ""
    for pixel_value in grayscale_image.getdata():
        ascii_str += ASCII_CHARS[int(pixel_value / 255 * (len(ASCII_CHARS) - 1))]
    # Split ASCII string into lines of the specified width
    ascii_lines = [ascii_str[i:i + width] for i in range(0, len(ascii_str), width)]
    return "\n".join(ascii_lines)

def gif_to_ascii(file_path):
    try:
        # Open the local GIF file
        frames = Image.open(file_path)
    except IOError:
        print(f"Failed to open GIF file at {file_path}")
        return

    # Convert GIF frames to ASCII frames
    ascii_frames = []
    for frame in ImageSequence.Iterator(frames):
        # Convert each frame to ASCII art
        ascii_art = image_to_ascii(frame)
        ascii_frames.append(ascii_art)

    # Determine the maximum width and height of the frames
    max_width = max(len(frame.splitlines()[0]) for frame in ascii_frames)
    max_height = max(len(frame.splitlines()) for frame in ascii_frames)

    while True:
        # Display ASCII frames in the terminal
        for i in range(len(ascii_frames)):
            sys.stdout.write("\033[H")  # Move cursor to the top left corner
            # Center the ASCII frame within the terminal
            frame_lines = ascii_frames[i].splitlines()
            top_margin = (max_height - len(frame_lines)) // 2
            for _ in range(top_margin):
                print()  # Print empty lines for top margin
            for line in frame_lines:
                left_margin = (max_width - len(line)) // 2
                print(" " * left_margin + line)
            sys.stdout.flush()
            time.sleep(0.05)  # Adjust the speed of animation as needed
            sys.stdout.write("\033[J")  # Clear the rest of the terminal below the frame

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gif_to_ascii.py <gif_file_path>")
        sys.exit(1)

    gif_file_path = sys.argv[1]
    gif_to_ascii(gif_file_path)
