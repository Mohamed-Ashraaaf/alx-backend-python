#!/usr/bin/env python3
"""Async Comprehensions"""

import asyncio
import random
from typing import AsyncGenerator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """Async Comprehensions"""
    async for i in async_generator():
        yield i
