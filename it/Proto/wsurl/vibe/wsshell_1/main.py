import asyncio
from memory import Memory
from net import Net
from console import ConsoleUI
from automata import Automata

async def main():
    memory = Memory()
    net = Net()
    ui = ConsoleUI()
    automata = Automata(memory, net, ui)

    while True:
        line = await ui.input()
        await automata.handle(line)

if __name__ == "__main__":
    asyncio.run(main())