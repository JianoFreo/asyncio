# import asyncio

# async def fetch_data(id, sleep_time):
#     print(f"Coroutine {id} starting to fetch data.")
#     await asyncio.sleep(sleep_time) # Simulate a network request or IO operation
#     return {"id": id, "data": f"Sample data from coroutine {id}"}

# async def main():
#     tasks = []
#     async with asyncio.TaskGroup() as tg:
#         for i, sleep_time in enumerate( [2, 1, 3], start=1):
#             task = tg.create_task(fetch_data(i, sleep_time))
#             tasks.append(task)

#     # After the Task Group block, all tasks have completed
#     results = [task. result() for task in tasks]

#     for result in results:
#         print(f"Received result: {result}")

# asyncio.run(main() )

import asyncio

records = {}

async def fetch_data(your_id, name, secs):
    for i in range(secs, -1, -1):
        await asyncio.sleep(1)
        print(f"running id {your_id} In T minus {i} seconds... ")
    name = name + " the GOAT"
    if (your_id % 10) < 5:
        new_id = str(your_id) + "M"
    else:
        new_id = str(your_id) + "F"
    return [new_id, name]

async def main():
    ids = []
    names = []
    secses = []
    while True:
        try:
            your_id = int(input("what is your given id? "))
            name = str(input("what is your name? lets reverse it "))
            secs = int(input("how many seconds until it returns? "))
            
            ids.append(your_id)    
            names.append(name)
            secses.append(secs)
            
            choice = input("enter q to quit ")
            if choice.lower() == "q":
                break
        except ValueError as e:
            print(f"Wrong value son {e}")
    tasks = []
    # dicts = {"people":{}}
    async with asyncio.TaskGroup() as tg:
        for i, j, k in zip(ids, names, secses):
            task = tg.create_task(fetch_data(i, j, k))
            tasks.append(task)
        # results = await tasks
        # tasks is a list, and Python can’t await a list. 
        # You need to await all tasks together.
        
        # Replace that line with:
        results = await asyncio.gather(*tasks)
        print(results)
        
        # tg.create_task(...) → creates tasks running concurrently 
        # tasks → just a list of those tasks
        # asyncio.gather(*tasks) → waits for all of them and collects results
                
                
            # task1 = asyncio.create_task(fetch_data(your_id, name, secs))
            # task2 = asyncio.create_task(fetch_data(your_id + 1, name + " II", secs))
            # print("processing...")
            # result1 = await task1
            # result2 = await task2
            
            # records[result1[0]] = result1[1]
            # records[result2[0]] = result2[2]
            
            # print(records)
        
                
asyncio.run(main())

