import asyncio
import websockets

class Net:
    def __init__(self):
        self.websocket = None

    async def connect(self, url):
        self.websocket = await websockets.connect(url)

    async def send(self, message):
        if self.websocket:
            await self.websocket.send(message)

    async def receive(self):
        if self.websocket:
            return await self.websocket.recv()

    async def close(self):
        if self.websocket:
            await self.websocket.close()