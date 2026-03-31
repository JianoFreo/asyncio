import asyncio

async def task(name):
    for i in range(3):
        print(f"{name} step {i+1}")
        await asyncio.sleep(1)

async def main():
    t1 = asyncio.create_task(task("Task A"))
    t2 = asyncio.create_task(task("Task B"))
    
    # t1 = await asyncio.create_task(task("Task A"))
    # t2 = await asyncio.create_task(task("Task B"))
    # Task A is created ✅
    # Then immediately awaited ❗
    # So the program stops and runs Task A fully

    # supposed output so far:

    # Task A step 1
    # Task A step 2
    # Task A step 3
    
    await t1
    await t2
    # await asyncio.gather(t2, t1)
    # Both tasks are already scheduled
    # gather() does NOT control execution order
    # It just waits for them to finish
    print("Tasks ended")

asyncio.run(main())