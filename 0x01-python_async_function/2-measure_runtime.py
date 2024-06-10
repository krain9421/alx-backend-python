#!/usr/bin/env python3
"""Module that measures the execution time of a coroutine"""

import asyncio
import time
# from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function that that measures the total execution time for
        ` wait_n(n, max_delay)`, and returns total_time / n
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed
