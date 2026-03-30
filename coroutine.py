import asyncio

# Coroutine function
async def main():
    print("Start of main coroutine")
    
# main() -> Coroutine object

# Run the main coroutine
asyncio.run(main())
# asyncio.run starts the event loop