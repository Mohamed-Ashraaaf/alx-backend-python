#!/usr/bin/env python3
"""
Asynchro coroutine that spawn multiple wait_random.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawn wait_random n times with the specified max_de
    """
    delays = [asyncio.create_task(wait_random(max_delay))for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
