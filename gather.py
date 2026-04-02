import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time) # Simulate a network request or IO operation
    # Return some data as a result
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main() :
# Run coroutines concurrently and gather their return values
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3)) #returns a list
    # Your code is basically the same as this:
    # t1 = asyncio.create_task(fetch_data(1, 2))
    # t2 = asyncio.create_task(fetch_data(2, 1))
    # t3 = asyncio.create_task(fetch_data(3, 3))

    # results = await asyncio.gather(t1, t2, t3)
    print(results)
    # Process the results
    for result in results:
        print(f"Received result: {result}")

# Run the main coroutine
asyncio.run(main())