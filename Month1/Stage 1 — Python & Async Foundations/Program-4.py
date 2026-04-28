# asyncio basics — async/await patterns

import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World, welcome to the world of Python and Asyncio!")

asyncio.run(main())

# asyncio gather example
async def task1():
    await asyncio.sleep(1)
    return "Task 1 completed"

async def task2():
    await asyncio.sleep(2)
    return "Task 2 completed"

async def main():
    result = await asyncio.gather(task1(), task2())
    print(result)

asyncio.run(main())