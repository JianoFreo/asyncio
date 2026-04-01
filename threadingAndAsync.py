# import asyncio
# import threading

# def stopper():
#     while True:
#         stopped = input()
#         if stopped == "":
#             break

# async def fetch_data(task, inputs, id):
#     for i in range(inputs):
#         print(f"Processing task {task} input {i + 1}")
#         await asyncio.sleep(1)
#         inputs -= 1
#         if inputs == 0:
#             break
#     return id + 1

# async def main():
#     inputs = int(input("Input the amount of inputs "))
#     id = int(input("input your ID "))

#     taskA = await fetch_data("taskA", inputs, id)
#     fixed_data = await fetch_data("fixed data", inputs, 10)

#     print(f"your Id is {taskA} and the fixed data id is {fixed_data}")

# def run_async():
#     asyncio.run(main())

# # start threads properly
# threading.Thread(target=run_async, daemon=True).start()
# threading.Thread(target=stopper, daemon=False).start()

import asyncio
import threading

stop_event = threading.Event()

def stopper():
    while True:
        stopped = input()
        if stopped == "":
            stop_event.set()
            break

async def fetch_data(task, inputs, id):
    for i in range(inputs):
        if stop_event.is_set():
            print(f"{task} stopped early")
            return id + 1

        print(f"Processing task {task} input {i + 1}")
        await asyncio.sleep(1)

    return id + 1

async def main():
    inputs = int(input("Input the amount of inputs "))
    id = int(input("input your ID "))

    t1 = asyncio.create_task(fetch_data("taskA", inputs, id))
    t2 = asyncio.create_task(fetch_data("fixed data", inputs, 10))

    taskA = await t1
    fixed_data = await t2

    print(f"your Id is {taskA} and the fixed data id is {fixed_data}")

# start stopper thread
threading.Thread(target=stopper, daemon=True).start()

# run asyncio normally (IMPORTANT)
asyncio.run(main())