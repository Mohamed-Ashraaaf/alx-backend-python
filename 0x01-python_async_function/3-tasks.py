#!/usr/bin/env python3
"""
Creating an asyncio.Task from an async function.
"""

import asyncio
from typing import Any, Awaitable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[int]:
    """
    Create an asyncio.Task from the wait_random function
    Args:
        max_delay (int): The maximum delay for wait_random
    Returns:
        asyncio.Task: An asyncio task
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    asyncio.run(task_wait_random(5))
