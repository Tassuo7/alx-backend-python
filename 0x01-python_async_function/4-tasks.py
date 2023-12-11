#!/usr/bin/env python3
"""
Take the code from wait_n
and alter it into a new function task_wait_n
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The code is nearly identical to wait_n
    except task_wait_random is being called.
    """
    tsks = []
    dlys = []

    for i in range(n):
        tsk = task_wait_random(max_delay)
        tsks.append(tsk)

    for tsk in asyncio.as_completed((tsks)):
        dly = await tsk
        dlys.append(dly)

    return dlys
