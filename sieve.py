import sys
import time
import matplotlib.pyplot as plt

# Function to find prime numbers using Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

# Measure execution time for each Python implementation
def benchmark_sieve(n):
    results = {}

    # CPython benchmark
    start_time = time.time()
    sieve_of_eratosthenes(n)
    results['CPython'] = time.time() - start_time
    print(f"CPython: {results['CPython']} seconds")

    # PyPy benchmark (ensure you run this with pypy command)
    if 'pypy' in sys.version:
        start_time = time.time()
        sieve_of_eratosthenes(n)
        results['PyPy'] = time.time() - start_time
        print(f"PyPy: {results['PyPy']} seconds")

    # Jython benchmark (ensure you run this with jython command)
    if 'jython' in sys.version:
        start_time = time.time()
        sieve_of_eratosthenes(n)
        results['Jython'] = time.time() - start_time
        print(f"Jython: {results['Jython']} seconds")

    return results

def plot_sieve(results, n):
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.bar(results.keys(), results.values(), color=['blue', 'green', 'red'])
    plt.xlabel('Python Implementation')
    plt.ylabel('Time (seconds)')
    plt.title(f'Sieve of Eratosthenes Benchmark Comparison (n={n})')
    plt.savefig('sieve_benchmark.png')
    plt.close()

if __name__ == '__main__':
    n = 100000  # Adjust n as needed for your benchmarking purposes
    results = benchmark_sieve(n)
    plot_sieve(results, n)
    print(f"Benchmark results for Sieve with n={n}: {results}")
