import asyncio
import json
from serial.tools import list_ports
from websockets.server import serve, WebSocketServerProtocol
from detect_emotion import DetectEmotion

def status_code():
    return {
        "status": "success",
        "code": 200
    }

def create_message():
    return {

    }

def create_init_message():
    return {
        **create_message()
    }

def read_messsage(message):
    json.loads(message)

async def handler(websocket: WebSocketServerProtocol):
    await websocket.send(json.dumps(create_init_message()))

    async for message in websocket:
        read_messsage(message)
        await websocket.send("Message received!")

async def main():
    print("Starting websocket server...")
    async with serve(handler, 'localhost', 3001):
        print("Websocket server running on port 3001\n")

        await asyncio.Future()  # run forever

asyncio.run(main())