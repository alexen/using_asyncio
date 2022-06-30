#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import time


async def very_long_function():
    print('I am going to work for a very long time')
    await asyncio.sleep(24*60*60)


async def main():
    print('[{}]: Let\'s start long-working function'.format(time.strftime('%T')))
    try:
        await asyncio.wait_for(very_long_function(), timeout=5.0)
    except asyncio.TimeoutError:
        print('!! Oops! Time is up! Bye-bye!')
    print('[{}]: We are done!'.format(time.strftime('%T')))


asyncio.run(main())
