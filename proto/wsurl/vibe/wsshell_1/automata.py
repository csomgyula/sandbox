import re

class Automata:
    def __init__(self, memory, net, ui):
        self.memory = memory
        self.net = net
        self.ui = ui

    async def handle(self, line):
        if line.startswith("connect"):
            match = re.match(r"connect (.+)", line)
            if match:
                url = match.group(1)
                await self.net.connect(url)
                self.memory.connected = True
                self.ui.output(f"Connected to {url}")

        elif line.startswith("send"):
            match = re.match(r"send (.+)", line)
            if match:
                message = match.group(1)
                await self.net.send(message)
                self.ui.output(f"Sent: {message}")

        elif line == "receive":
            msg = await self.net.receive()
            self.memory.last_message = msg
            self.ui.output(f"Received: {msg}")

        elif line == "exit":
            await self.net.close()
            self.ui.output("Connection closed.")
            exit(0)

        else:
            self.ui.output("Unknown command")