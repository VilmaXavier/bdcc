import sys
import time
import matplotlib.pyplot as plt

# Function to calculate Fibonacci using recursion (single-threaded)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Measure execution time for each Python implementation
def benchmark_fibonacci(n):
    results = {}

    # CPython benchmark
    start_time = time.time()
    fibonacci(n)
    results['CPython'] = time.time() - start_time
    print(f"CPython: {results['CPython']} seconds")

    # PyPy benchmark (ensure you run this with pypy command)
    if 'pypy' in sys.version:
        start_time = time.time()
        fibonacci(n)
        results['PyPy'] = time.time() - start_time
        print(f"PyPy: {results['PyPy']} seconds")

    # Jython benchmark (ensure you run this with jython command)
    if 'jython' in sys.version:
        start_time = time.time()
        fibonacci(n)
        results['Jython'] = time.time() - start_time
        print(f"Jython: {results['Jython']} seconds")

    return results

def plot_fibonacci(results, n):
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.bar(results.keys(), results.values(), color=['blue', 'green', 'red'])
    plt.xlabel('Python Implementation')
    plt.ylabel('Time (seconds)')
    plt.title(f'Fibonacci Benchmark Comparison (n={n})')
    plt.savefig('fibonacci_benchmark.png')
    plt.close()

if __name__ == '__main__':
    n = 35  # Adjust n as needed for your benchmarking purposes
    results = benchmark_fibonacci(n)
    plot_fibonacci(results, n)
    print(f"Benchmark results for Fibonacci with n={n}: {results}")
