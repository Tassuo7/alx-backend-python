#!/usr/bin/env python3
"""
using async_comprehension from the previous file
write a measure_runtime coroutine
that will execute async_comprehension four times in parallel
"""
import asyncio
import random
from typing import Generator, List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    should measure the total runtime and return it
    """
    ti = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    tf = asyncio.get_running_loop().time()
    return tf - ti
