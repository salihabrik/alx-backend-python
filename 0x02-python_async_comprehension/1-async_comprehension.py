#!/usr/bin/env python3
"""
Module documentation goes here
"""

import asyncio
from typing import List
from itertools import islice

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the list of 10 random numbers.

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [num async for num in islice(async_generator(), 10)]
