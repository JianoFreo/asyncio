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
    async with asyncio.TaskGroup() as tg:
        for i, j, k in zip(ids, names, secses):
            task = tg.create_task(fetch_data(i, j, k))
            tasks.append(task)
        results = await tasks
        print(results)