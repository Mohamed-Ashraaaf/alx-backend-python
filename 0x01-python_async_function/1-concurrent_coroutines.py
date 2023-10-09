#!/usr/bin/env python3
"""
Asynchro coroutine that spawn multiple wait_random.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_del
    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.
    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    return await asyncio.gather(*delays)
