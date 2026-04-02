# #======= Provided version ===============
# import asyncio

# async def fetch_data(id, sleep_time):
#     print(f"Coroutine {id} starting to fetch data.")
#     await asyncio.sleep(sleep_time)
#     return {"id": id, "data": f"Sample data from coroutine {id}"}



# async def main():
# # Create tasks for running coroutines concurrently
#     task1 = asyncio.create_task(fetch_data(1, 2))
#     task2 = asyncio.create_task(fetch_data(2, 3))
#     task3 = asyncio.create_task(fetch_data(3, 1))

#     result1 = await task1
#     result2 = await task2
#     result3 = await task3

#     print(result1, result2, result3)

# asyncio.run(main())


# import asyncio

# async def fetch_data(id, sleep_time, name):
#     print(f"Starting to fetch data of ID: {id}")
#     await asyncio.sleep(sleep_time)
#     print(f"reversed name of {name} is {name[::-1]} and your new id is {id + 1}")
#     return f"Hello {name[::-1]}, your new id is {id + 1}"
    
# async def main():
#     while True:
#         try:
#             raw_id = int(input("What is your ID: "))
#             if raw_id == "":
#                 break

#             raw_sleep = int(input("How long is the sleep time: "))
#             if raw_sleep == "":
#                 break

#             name = input("What is your name?, lets reverse it: ")
#             if name == "":
#                 break
            
#             task = asyncio.create_task(fetch_data(raw_id, raw_sleep, name))
            
#             result = await task
#             asyncio.create_task(main())
#             print(result)
#         except ValueError:
#             print("Please write a right value")
        
# asyncio.run(main())


import asyncio

async def fetch_data(id, sleep_time, name):
    print(f"Starting to fetch data of ID: {id}")
    await asyncio.sleep(sleep_time)
    print(f"reversed name of {name} is {name[::-1]} and your new id is {id + 1}")
    return f"Hello {name[::-1]}, your new id is {id + 1}"

async def main():
    tasks = []

    while True:
        try:
            raw_id = input("What is your ID: ")
            if raw_id == "":
                break

            raw_sleep = input("How long is the sleep time: ")
            if raw_sleep == "":
                break

            name = input("What is your name?, lets reverse it: ")
            if name == "":
                break

            id = int(raw_id)
            sleep_time = int(raw_sleep)

            # start task but DON'T await
            task = asyncio.create_task(fetch_data(id, sleep_time, name))
            tasks.append(task)

        except ValueError:
            print("Please write a right value")

    # wait for all tasks at the end
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

asyncio.run(main())