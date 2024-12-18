import time
import sys
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

# Example Fibonacci function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Parallel Fibonacci using ProcessPoolExecutor
def parallel_fibonacci(n):
    def worker(start, end):
        return [fibonacci(i) for i in range(start, end)]

    num_processes = 4
    step = n // num_processes
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = executor.map(worker, range(0, n, step), range(step, n, step))

    # Flatten the result list
    fibonacci_numbers = []
    for result in results:
        fibonacci_numbers.extend(result)
    return fibonacci_numbers

# Sieve of Eratosthenes (single-threaded)
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(limit + 1) if sieve[i]]

# Parallel Sieve of Eratosthenes using ProcessPoolExecutor
def parallel_sieve_of_eratosthenes(limit):
    def sieve_worker(start, end):
        sieve = [True] * (end - start + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(end**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, end + 1, i):
                    sieve[j] = False
        return [num for num, prime in enumerate(sieve, start=start) if prime]

    num_processes = 4
    step = limit // num_processes
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = executor.map(sieve_worker, range(0, limit, step), range(step, limit, step))

    primes = []
    for result in results:
        primes.extend(result)
    return primes

# Benchmarking function for Fibonacci and Sieve of Eratosthenes
def benchmark_algorithm(implementation, n_fibonacci):
    print(f"Testing with {implementation} implementation")
    
    # Test Fibonacci
    start_time = time.time()
    fibonacci(n_fibonacci)
    end_time = time.time()
    print(f"Fibonacci Time (Single): {end_time - start_time}")

    # Test Parallel Fibonacci
    start_time = time.time()
    parallel_fibonacci(n_fibonacci)
    end_time = time.time()
    print(f"Fibonacci Time (Parallel): {end_time - start_time}")
    
    # Test Sieve of Eratosthenes
    start_time = time.time()
    sieve_of_eratosthenes(100000)
    end_time = time.time()
    print(f"Sieve Time (Single): {end_time - start_time}")

    # Test Parallel Sieve of Eratosthenes
    start_time = time.time()
    parallel_sieve_of_eratosthenes(100000)
    end_time = time.time()
    print(f"Sieve Time (Parallel): {end_time - start_time}")
    
# Create benchmark charts
def create_benchmark_charts():
    n_fibonacci = 35
    implementations = ["Python", "PyPy", "Jython"]

    # Create empty lists to store benchmark results
    fibonacci_single_time = []
    fibonacci_parallel_time = []
    sieve_single_time = []
    sieve_parallel_time = []

    for implementation in implementations:
        benchmark_algorithm(implementation, n_fibonacci)

        # Append results for graphing (dummy times used here for illustration)
        fibonacci_single_time.append(1.5)  # Replace with actual measured times
        fibonacci_parallel_time.append(1.0)  # Replace with actual measured times
        sieve_single_time.append(0.1)  # Replace with actual measured times
        sieve_parallel_time.append(0.2)  # Replace with actual measured times

    # Plot results
    plt.figure(figsize=(10, 5))
    plt.plot(implementations, fibonacci_single_time, label="Fibonacci Single", marker='o')
    plt.plot(implementations, fibonacci_parallel_time, label="Fibonacci Parallel", marker='o')
    plt.plot(implementations, sieve_single_time, label="Sieve Single", marker='o')
    plt.plot(implementations, sieve_parallel_time, label="Sieve Parallel", marker='o')

    plt.xlabel("Implementation")
    plt.ylabel("Time (Seconds)")
    plt.title("Benchmark Results")
    plt.legend()
    plt.show()

# Run benchmarks and create charts
def run_benchmarks():
    create_benchmark_charts()

if __name__ == "__main__":
    run_benchmarks()
