import asyncio

records = {}

async def fetch_data(your_id, name, secs):
    print("processing...")
    for i in range(secs, -1, -1):
        await asyncio.sleep(1)
        print(f"In T minus {i} seconds... ")
    reversed_name = name[::-1]
    if (your_id % 10) < 5:
        new_id = str(your_id) + "M"
    else:
        new_id = str(your_id) + "F"
    return new_id, reversed_name

async def main():
    while True:
        try:
            your_id = int(input("what is your given id? "))
            name = str(input("what is your name? lets reverse it "))
            secs = int(input("how many seconds until it returns? "))
             
            task = asyncio.create_task(fetch_data(your_id, name, secs))
            result = await task
            records[result[0]] = result[1]
            print(records)
        except ValueError as e:
            print(f"Wrong value son {e}")
            
asyncio.run(main())