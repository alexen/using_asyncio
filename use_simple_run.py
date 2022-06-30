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

    await say_after(1, "Hello")
    await say_after(2, "The")
    await say_after(3, "Wonderful")
    await say_after(4, "World!")

    print(">> FINISH! (time: {} s)".format(time.time() - start))


asyncio.run(main())
