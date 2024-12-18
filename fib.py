import sys
import time

# Optimized Fibonacci using iteration to avoid recursion limit issues
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Measure execution time for each Python implementation
def benchmark_fibonacci(n):
    results = {}
    log_filename = "fibonacci_times.txt"  # Log file to store results

    # Print the current Python version and interpreter
    print("Running on: {}".format(sys.version))

    # Check the interpreter and run the respective block
    if 'pypy' in sys.version.lower():  # Check for PyPy
        print("PyPy block executed")
        start_time = time.time()
        fibonacci(n)
        end_time = time.time()
        pypy_time = end_time - start_time
        results['PyPy'] = pypy_time
        print("PyPy - Start: {}, End: {}, Time: {} seconds".format(start_time, end_time, pypy_time))
        
    elif sys.version_info[0] == 3:  # Check for CPython (Python 3.x)
        print("CPython block executed")
        start_time = time.time()
        fibonacci(n)
        end_time = time.time()
        cpython_time = end_time - start_time
        results['CPython'] = cpython_time
        print("CPython - Start: {}, End: {}, Time: {} seconds".format(start_time, end_time, cpython_time))

    else:
        print("Unknown interpreter: {}".format(sys.version))

    # Write the results to a text file
    with open(log_filename, 'a') as log_file:
        log_file.write("Results for Fibonacci with n={}: \n".format(n))
        for interpreter, run_time in results.items():
            log_file.write("{} - Time: {} seconds\n".format(interpreter, run_time))
        log_file.write("\n")  # Newline for separation between runs

    return results

if __name__ == '__main__':
    n = 35  # Adjust n as needed for your benchmarking purposes
    results = benchmark_fibonacci(n)
    print("Benchmark results stored in fibonacci_times.txt")
