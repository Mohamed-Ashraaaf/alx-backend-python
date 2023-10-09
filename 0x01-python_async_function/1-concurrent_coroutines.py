#!/usr/bin/env python3
"""
Asynchronous coroutine that spawns multiple instances of wait_random.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay in seconds
    Returns:
        List[float]: List of delays in ascending order
    """
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    gathered_delays = await asyncio.gather(*delays)
    return sorted(gathered_delays)
