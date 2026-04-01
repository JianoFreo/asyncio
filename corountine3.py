import asyncio

async def fetch_data(task, inputs, id):
    for i in range(inputs):
        print(f"Processing task {task} input {i + 1}")
        await asyncio.sleep(1)
        inputs -= 1
        if inputs == 0:
            break
    return id + 1
    
    
async def main():
    inputs = int(input("Input the amount of inputs "))
    id = int(input("input your ID "))
    # This comment is sequential not concurrent (Async)
    # taskA frist then taskB
    # taskA = fetch_data("Task A",inputs, id)
    # taskB = fetch_data("Task B", inputs, 100 )
    t1 = fetch_data("Task A",inputs, id)
    t2 = fetch_data("Task B", inputs, 100 )
    taskA = await t1
    taskB = await t2
    
    print(f"Your Id number is {taskA} compared to the id number of task b {taskB}")
    
asyncio.run(main())
####------------one below is basically the same but without asyncio-------------
####--------It is no concurrent because im nonly running one task-------------
# import time

# def fetch_data(inputs, id):
#     for i in range(inputs):
#         print(f"Processing input {i + 1}")
#         time.sleep(1)
#         inputs -= 1
#         if inputs == 0:
#             break
#     return id + 1
    
    
# def main():
#     inputs = int(input("Input the amount of inputs "))
#     id = int(input("input the previous ID "))
#     result = fetch_data(inputs, id)
#     print(f"Your Id number is {result}")
    
# main()