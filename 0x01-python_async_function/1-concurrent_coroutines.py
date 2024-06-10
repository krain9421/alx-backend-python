#!/usr/bin/env python3
"""Module that executes multiple coroutines at the same time"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Routine that takes 2 arguments and returns
        a list of delays
    """
    # Spawn wait_random n times
    lst = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))

    return sorted(lst)
