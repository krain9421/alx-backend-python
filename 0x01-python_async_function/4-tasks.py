#!/usr/bin/env python3
"""Module that alters and existing coroutine"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Routine that takes 2 arguments and returns
        a list of delays
    """
    # Spawn task_wait_random n times
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    # lst = await asyncio.gather
    # (*(task_wait_random(max_delay) for i in range(n)))
    lst = await asyncio.gather(*tasks)
    return sorted(lst)
