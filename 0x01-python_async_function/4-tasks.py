#!/usr/bin/env python3
"""
Creating asyncio.Tasks from a list of async functions.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create a list of asyncio.Tasks from task_wait_random
    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for task_wait_random
    Returns:
        List[float]: A list of floats representing the delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
