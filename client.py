import asyncio
import websockets
import sys

async def receive_ascii_frames(gif_url):
    uri = "ws://gif-to-ascii-cc9ca28d7a01.herokuapp.com"
    async with websockets.connect(uri) as websocket:
        await websocket.send(gif_url)
        
        try:
            while True:
                frame = await websocket.recv()
                if frame.startswith("Error:"):
                    print(frame)
                    break
                print("\033[H\033[J" + frame)  # Clear the terminal and print frame
                await asyncio.sleep(0.1)  # Adjust for frame rate
        except websockets.ConnectionClosed:
            print("Connection closed")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <gif_url>")
        sys.exit(1)

    gif_url = sys.argv[1]
    asyncio.run(receive_ascii_frames(gif_url))
