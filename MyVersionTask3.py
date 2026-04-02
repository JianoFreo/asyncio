import asyncio
import threading

records = {}

async def fetch_data(your_id, name, secs):
    for i in range(secs, -1, -1):
        await asyncio.sleep(1)
        print(f"running id {your_id} In T minus {i} seconds... ")
    reversed_name = name[::-1]
    if (your_id % 10) < 5:
        new_id = str(your_id) + "M"
    else:
        new_id = str(your_id) + "F"
    return new_id, reversed_name, name

async def main():
    while True:
        try:
            your_id = int(input("what is your given id? "))
            name = str(input("what is your name? lets reverse it "))
            secs = int(input("how many seconds until it returns? "))
             
            task1 = asyncio.create_task(fetch_data(your_id, name, secs))
            task2 = asyncio.create_task(fetch_data(your_id + 1, name + " II", secs))
            print("processing...")
            result1 = await task1
            result2 = await task2
            
            records[result1[0]] = result1[1]
            records[result2[0]] = result2[2]
            
            print(records)
        except ValueError as e:
            print(f"Wrong value son {e}")
            
def coroutines():
    asyncio.run(main())

def stopper():
    input("press enter to stop")
    
thread1 = threading.Thread(target=stopper, daemon=False)    
thread2 = threading.Thread(target=coroutines, daemon=True)

thread1.start()
thread2.start()
