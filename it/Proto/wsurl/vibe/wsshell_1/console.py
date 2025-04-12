import asyncio
class ConsoleUI:
    async def input(self):
        return await asyncio.get_event_loop().run_in_executor(None, input, "> ")

    def output(self, message):
        print(message)