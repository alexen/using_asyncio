#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import time


def timestamp():
    return time.strftime('%T')


async def coro(name, delay):
    print(f'[{timestamp()}]: Coro {name} is going to work {delay} seconds')
    await asyncio.sleep(delay)
    return name


async def main():
    print(f'[{timestamp()}]: Starting loop')

    data = [
        ('Alice', 7),
        ('Bob',   3),
        ('Clark', 5)
        ]

    for completed in asyncio.as_completed([coro(name, delay) for name, delay in data]):
        print(f'[{timestamp()}]: Awaiting some coro')
        name = await completed
        print(f'[{timestamp()}]: Coro {name} completed!')


start = time.time()
asyncio.run(main())
print('Time elapsed: {}'.format(time.time() - start))
