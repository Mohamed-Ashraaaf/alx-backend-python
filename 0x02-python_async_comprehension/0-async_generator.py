#!/usr/bin/env python3
"""
Async generator that yields random numbers
"""

import asyncio
import random


async def async_generator():
    """
    Coroutine that yields random numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
