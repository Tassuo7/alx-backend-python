#!/usr/bin/env python3
"""
use wait_random from the previous python file
and write an async routine
"""
import asyncio
from typing import List
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in 2 int arguments
    spawn wait_random n times with the specified max_delay
    return the list of all the delays in ascending order
    """
    dt = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    lst = [await task for task in asyncio.as_completed(dt)]
    return lst
