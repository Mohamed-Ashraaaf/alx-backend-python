#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds.
    
    Args:
        max_delay (int): Maximum delay in seconds (default 10).

    Returns:
        float: Random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
