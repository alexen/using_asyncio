#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(f'After {delay} I am saying {what}')


async def main():
    start = time.time()

    print(">> START!")

    tasks = [
        asyncio.create_task(say_after(1, "Hello")),
        asyncio.create_task(say_after(2, "The")),
        asyncio.create_task(say_after(3, "Wonderful")),
        asyncio.create_task(say_after(4, "World!"))
    ]

    for task in tasks:
        await task

    print(">> FINISH! (time: {} s)".format(time.time() - start))


asyncio.run(main())
