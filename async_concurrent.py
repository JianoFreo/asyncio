import asyncio

async def task(name):
    for i in range(3):
        print(f"{name} step {i+1}")
        await asyncio.sleep(1)

async def main():
    t1 = asyncio.create_task(task("Task A"))
    t2 = asyncio.create_task(task("Task B"))

    print("Tasks started")

    await t1
    await t2

asyncio.run(main())