#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import time


async def good_task(name, count, delay):
    for n in range(1, count+1):
        print("[{}]: Task <{}> is doing work #{}/{}".format(time.strftime("%T"), name, n, count))
        await asyncio.sleep(delay)
    print("[{}]: Task <{}> is done".format(time.strftime("%T"), name))
    return dict(
        task_name = name,
        status = 'OK'
        )


async def bad_task(name, count, delay):
    print("[{}]: Task <{}> is doing work #{}/{}".format(time.strftime("%T"), name, 1, count))
    await asyncio.sleep(delay)
    raise RuntimeError(f"Moo-ha-ha-ha-ha!!! I am {name}!!!")


async def main():
    start_time = time.time()

    print(">> START!")

    try:
        results = await asyncio.gather(
            good_task("Alice", 5, 1),
            good_task("Clark", 2, 3),
            bad_task("DrEvil", 3, 1),
            return_exceptions = True
        )
        print(f">> Results: {results}")
    except RuntimeError as e:
        print(f"Wow! Some task raised an exception: {e}")

    print(">> FINISH (time: {})!".format(time.time() - start_time))


asyncio.run(main())
