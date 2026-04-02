import asyncio

async def fetch_data(your_id, name, secs):
    print("Processing data...")
    await asyncio.sleep(secs)
    # print(f"your id is {your_id} lets add 1 to that now its {your_id + 1}")
    # print(f"and your reverse name is {name} and lets reverse that now its {name[::-1]}")
    your_id = your_id + 1
    name = name[::-1]
    return your_id, name
    

async def main():
    results = {"reversed_identity": {}}
    while True:
        try:
            id = int(input("your id number? "))
            name = input("whats your name? ")
            secs = int(input("how many seconds should it last? "))
            if id == "" or name == "" or secs == "":
                break
            
            task = asyncio.create_task(fetch_data(id, name, secs))
            result = await task

            result = await task
            results["reversed_identity"][result[0]] = result[1]
        except ValueError:
            print("Wrong type son")
            break
    print(results)
        
asyncio.run(main())