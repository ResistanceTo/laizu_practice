import asyncio
from collections.abc import AsyncGenerator, Awaitable


# def function():
#     return 1

# def generator():
#     yield 1

# async def async_function():
#     return 1

# async def async_generator():
#     yield 1

# import types
# print(type(function) is types.FunctionType)
# print(type(generator()) is types.GeneratorType)
# print(type(async_function()) is types.CoroutineType)
# print(type(async_generator()) is types.AsyncGeneratorType)

# print(async_function().send(None))

# try:
#     async_function().send(None)
# except StopIteration as e:
#     print(e.value)

# def run(coroutine):
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         return e.value

# async def async_function():
#     return 1

# async def await_coroutine():
#     result = await async_function()
#     print(result)
    
# run(await_coroutine())  

from time import sleep
import random

class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for _ in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos

all_potatos = Potato.make(5)

async def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        potato = all_potatos.pop()
        yield potato
        count += 1
        if count == num:
            break

async def ask_for_potato():
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 10)))

async def buy_potatos():
    bucket = []
    async for p in take_potatos(13):
        bucket.append(p)
        print(f'Got potato {id(p)}...')

async def buy_tomatos():
    bucket = []
    async for p in take_potatos(13):
        bucket.append(p)
        print(f'Got tomato {id(p)}...')

def main():
    loop = asyncio.get_event_loop()
    # res = loop.run_until_complete(buy_potatos())
    res = loop.run_until_complete(asyncio.wait([buy_potatos(), buy_tomatos()]))
    loop.close()

main()
AsyncGenerator