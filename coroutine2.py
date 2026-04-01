import asyncio
import time

# Coroutine function
# async def main():
#     print("Start of main coroutine")
    
# # main() -> Coroutine object

# # Run the main coroutine
# asyncio.run(main())
# # asyncio.run starts the event loop

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print("Fetching data ... id:", id)
    await asyncio.sleep(delay) # Simulate an I/0 operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id} # Return some data

# Define another coroutine that calls the first coroutine
async def main(): # we have to define this as async because await only works under async
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1
    print(f"Received result: {result1}")

    result2 = await task2
    print(f"Received result: {result2}")

# Run the main coroutine
asyncio.run(main())
# What asyncio.run(main()) actually does
# it does three important things:

# Creates an event loop
# Runs your coroutine (main) inside that loop
# Closes the loop when done

# Think of it as the “engine” that actually executes your async code.