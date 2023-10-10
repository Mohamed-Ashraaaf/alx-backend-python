#!/usr/bin/env python3
"""
Async comprehension that collects 10 random numbers.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects rand numbers using async comprehension
    """
    return [i async for i in async_generator()]


async def main():
    print(await async_comprehension())


if __name__ == "__main__":
    asyncio.run(main())
