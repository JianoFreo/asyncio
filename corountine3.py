import asyncio
import threading
import time

async def fetch_data(inputs, id):
    for i in range(inputs):
        print(f"Processing input {i + 1}")
        await asyncio.sleep(1)
        inputs -= 1
        if inputs == 0:
            break
    return id + 1
    
    
async def main():
    inputs = int(input("Input the amount of inputs "))
    id = int(input("input the previous ID "))
    result = await fetch_data(inputs, id)
    print(f"Your Id number is {result}")
    
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