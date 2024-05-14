import time
import psutil
import os

def monitor_resources_and_time(func, *args, **kwargs):
    start_time = time.time()  # Start time
    process = psutil.Process(os.getpid())
    start_mem = process.memory_info().rss / (1024 * 1024)  # Memory usage in MB

    result = func(*args, **kwargs)  # Execute the function

    end_mem = process.memory_info().rss / (1024 * 1024)  # Memory usage in MB after execution
    end_time = time.time()  # End time

    print(f"Function execution time: {end_time - start_time} seconds")
    print(f"Memory used: {end_mem - start_mem} MB")
    return result

# Example function to evaluate
def example_function():
    # This is where you'd have the model process a query
    time.sleep(1)  # Simulating processing time
    return "Example output"

# Monitor and print the resource usage and time for example_function
monitor_resources_and_time(example_function)
