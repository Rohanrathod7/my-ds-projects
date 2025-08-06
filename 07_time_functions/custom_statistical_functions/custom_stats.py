import time
from collections import Counter
from contextlib import contextmanager
import math


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"📌 Function '{func.__name__}' called with arguments: {args}")
        result = func(*args, **kwargs)
        print(f"✅ Result: {result}\n")
        return result
    return wrapper


@contextmanager
def timer(task_name="Task"):
    start = time.time()
    yield
    end = time.time()
    print(f"⏱️ {task_name} completed in {end - start:.4f} seconds.\n")



@logger
def mean(data):
    """
    Calculates the mean of a list of numbers.
    """
    return sum(data) / len(data)

@logger
def median(data):
    """
    Returns the median value from a list.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

@logger
def mode(data):
    """
    Returns the mode of the list.
    """
    freq = Counter(data)
    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_freq]
    return modes if len(modes) > 1 else modes[0]

@logger
def variance(data):
    """
    Returns the sample variance of the list.
    """
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)

@logger
def std_dev(data):
    """
    Returns the standard deviation.
    """
    return math.sqrt(variance(data))
