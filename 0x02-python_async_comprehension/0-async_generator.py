#!/usr/bin/env python3
"""Defines a coroutine, one that takes no arguments"""

import asyncio
import random


async def async_generator() -> float:
    """
        The coroutine will loop 10 times,
        each time asynchronously wait 1 second,
        then yield a random number between 0 and 10.
    """
    for i in range(10):
        i = random.uniform(0, 10)
        yield i
        await asyncio.sleep(1)
