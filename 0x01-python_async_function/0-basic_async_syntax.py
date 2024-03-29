#!/usr/bin/env python3
"""
Asynchro coroutine that wait for random delay
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_del seconds
    Args:
        max_delay (int): Maximum delay in seconds def 10
    Returns:
        float: Random delay in seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
