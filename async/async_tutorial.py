import asyncio
import time


async def main1():
    print('hello')
    await asyncio.sleep(0.1)
    print('world')


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks
async def main2():

    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f'finished at {time.strftime("%X")}')


# The asyncio.TaskGroup class provides a more modern alternative to create_task()
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f'finished at {time.strftime("%X")}')

#The asyncio.run() function to run the top-level entry point “main()” function



######## Coroutines ###########
async def nested():
    return 42

async def main4():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it
    print(await nested())
    


####### Tasks ##################
# When a coroutine is wrapped into a Task with functions like asyncio.create_task()
# the coroutine is automatically scheduled to run soon:
async def nested():
    return 42

async def wild():
    await asyncio.sleep(0.1)
    return 41

async def main5():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task1 = asyncio.create_task(wild())
    task = asyncio.create_task(nested())
    
    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print(await task1)
    print(await task)
    await task

######### Futures ##########

async def main6():
    
    await function_that_returns_a_future_object()
    
    await asyncio.gather(
        function_that_returns_a_future_object(),
        nested()
    )
    

if __name__ == '__main__':
    # asyncio.run(main1())
    
    # asyncio.run(main2())
    
    # asyncio.run(main3())
    
    # asyncio.run(main4())
    
    # asyncio.run(main5())
    
    asyncio.run(main6())
