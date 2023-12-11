#!/usr/bin/env python3
"""
using wait_n into 2-measure_runtime
Create a measure_time function
"""


import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function with integers n and max_delay as arguments
    that measures the total execution time for wait_n
    and returns a float total_time / n
    """
    start_t = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_t = time.time()
    total_time = end_t - start_t
    return (total_time/n)
