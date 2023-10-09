#!/usr/bin/env python3
"""
Measuring the runtime of the wait_n function.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay in seconds
    Returns:
        float: Average execution time per call
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
