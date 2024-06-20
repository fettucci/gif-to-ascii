import asyncio
import websockets
from PIL import Image, ImageSequence
import logging
import os
import requests
from io import BytesIO

# Setup logging
logging.basicConfig(level=logging.INFO)

# ASCII characters used for grayscale conversion (from darkest to lightest)
ASCII_CHARS = "@#S%?*+;:,."

def image_to_ascii(image, width=100):
    height = int((image.height / image.width) * width)
    image = image.resize((width, height))
    grayscale_image = image.convert("L")
    ascii_str = "".join(ASCII_CHARS[int(pixel_value / 255 * (len(ASCII_CHARS) - 1))] for pixel_value in grayscale_image.getdata())
    ascii_lines = [ascii_str[i:i + width] for i in range(0, len(ascii_str), width)]
    return "\n".join(ascii_lines)

def gif_to_ascii(frames):
    try:
        gif = Image.open(BytesIO(frames))
    except IOError:
        logging.error("Failed to open GIF file")
        return []

    ascii_frames = [image_to_ascii(frame) for frame in ImageSequence.Iterator(gif)]
    return ascii_frames

async def send_ascii_frames(websocket, path):
    try:
        gif_url = await websocket.recv()
        logging.info(f"Received GIF URL: {gif_url}")

        # Fetch GIF data from the URL
        response = requests.get(gif_url)
        if response.status_code != 200:
            await websocket.send(f"Error: Failed to fetch GIF from {gif_url}")
            return
        
        gif_frames = response.content
        ascii_frames = gif_to_ascii(gif_frames)
        
        if not ascii_frames:
            await websocket.send("Error: Failed to convert GIF to ASCII")
            return

        while True:
            for frame in ascii_frames:
                await websocket.send(frame)
                await asyncio.sleep(0)  # Adjust for frame rate

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        await websocket.send(f"Error: {e}")

async def main():
    port = int(os.getenv("PORT", 8000))  # Use Heroku's dynamic port or default to 8000 for local testing
    async with websockets.serve(send_ascii_frames, "0.0.0.0", port):
        logging.info(f"WebSocket server started on ws://0.0.0.0:{port}")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
