#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio


async def main():
    print("Hello...")
    await asyncio.sleep(3)
    print("...world!")

asyncio.run(main())
