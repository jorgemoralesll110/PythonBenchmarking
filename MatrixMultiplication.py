import random
from time import time
import psutil
import os

# Function to perform matrix multiplication and measure time, memory, and CPU usage
def matrix_multiplication(n):
    # Create matrices A, B, and C
    A = [[random.random() for _ in range(n)] for _ in range(n)]
    B = [[random.random() for _ in range(n)] for _ in range(n)]
    C = [[0 for _ in range(n)] for _ in range(n)]

    # Get the current process to measure resource usage
    process = psutil.Process(os.getpid())

    # Measure initial memory (before the operation)
    initial_memory = process.memory_info().rss / 1024 ** 2  # Convert to MB

    # Measure initial CPU usage
    initial_cpu = process.cpu_percent(interval=None)

    # Measure start time
    start = time()

    # Matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    # Measure end time
    end = time()

    # Measure final memory (after the operation)
    final_memory = process.memory_info().rss / 1024 ** 2  # Convert to MB

    # Measure final CPU usage
    final_cpu = process.cpu_percent(interval=None)

    # Calculate metrics
    execution_time = end - start
    memory_used = final_memory - initial_memory
    cpu_used = final_cpu - initial_cpu

    # Print results for this matrix size
    print(f"\nMatrix size: {n}x{n}")
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Memory used: {memory_used:.2f} MB")
    print(f"CPU used: {cpu_used:.2f}%")

# Run the function for different matrix sizes
matrix_sizes = [10, 50, 150, 300, 450, 500, 650, 800, 1000]
for size in matrix_sizes:
    matrix_multiplication(size)
