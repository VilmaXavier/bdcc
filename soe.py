import sys
import time

# Optimized Sieve of Eratosthenes implementation
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
    log_filename = "sieve_times.txt"  # Log file to store results

    # Print the current Python version and interpreter
    print("Running on: {}".format(sys.version))

    # Check for PyPy3
    if 'pypy' in sys.version.lower():
        print("PyPy block executed")
        start_time = time.time()
        sieve_of_eratosthenes(n)
        end_time = time.time()
        pypy_time = end_time - start_time
        results['PyPy'] = pypy_time
        print("PyPy - Start: {}, End: {}, Time: {} seconds".format(start_time, end_time, pypy_time))

    # Check for Jython
    elif 'jython' in sys.version.lower():
        print("Jython block executed")
        start_time = time.time()
        sieve_of_eratosthenes(n)
        end_time = time.time()
        jython_time = end_time - start_time
        results['Jython'] = jython_time
        print("Jython - Start: {}, End: {}, Time: {} seconds".format(start_time, end_time, jython_time))

    # Check for IronPython
    elif 'ironpython' in sys.version.lower():
        print("IronPython block executed")
        start_time = time.time()
        sieve_of_eratosthenes(n)
        end_time = time.time()
        ironpython_time = end_time - start_time
        results['IronPython'] = ironpython_time
        print("IronPython - Start: {}, End: {}, Time: {} seconds".format(start_time, end_time, ironpython_time))

    # Check for MicroPython
    elif 'micropython' in sys.version.lower():
        print("MicroPython block executed")
        start_time = time.time()
        sieve_of_eratosthenes(n)
        end_time = time.time()
        micropython_time = end_time - start_time
        results['MicroPython'] = micropython_time
        print("MicroPython - Start: {}, End: {}, Time: {} seconds".format(start_time, end_time, micropython_time))

    # Check for Nuitka
    if 'nuitka' in sys.version.lower():
        print("Nuitka block executed")
        start_time = time.time()
        sieve_of_eratosthenes(n)
        end_time = time.time()
        nuitka_time = end_time - start_time
        results['Nuitka'] = nuitka_time
        print("Nuitka - Start: {}, End: {}, Time: {} seconds".format(start_time, end_time, nuitka_time))

    # Check for Anaconda Python
    elif 'anaconda' in sys.version.lower():
        print("Anaconda block executed")
        start_time = time.time()
        sieve_of_eratosthenes(n)
        end_time = time.time()
        anaconda_time = end_time - start_time
        results['Anaconda'] = anaconda_time
        print("Anaconda - Start: {}, End: {}, Time: {} seconds".format(start_time, end_time, anaconda_time))

    # Check for CPython (default implementation)
    elif sys.version_info[0] == 3:  # Python 3.x
        print("CPython block executed")
        start_time = time.time()
        sieve_of_eratosthenes(n)
        end_time = time.time()
        cpython_time = end_time - start_time
        results['CPython'] = cpython_time
        print("CPython - Start: {}, End: {}, Time: {} seconds".format(start_time, end_time, cpython_time))

    else:
        print("Unknown or unsupported interpreter: {}".format(sys.version))

    # Write the results to a text file
    with open(log_filename, 'a') as log_file:
        log_file.write("Results for Sieve of Eratosthenes with n={}: \n".format(n))
        for interpreter, run_time in results.items():
            log_file.write("{} - Time: {} seconds\n".format(interpreter, run_time))
        log_file.write("\n")  # Newline for separation between runs

    return results

if __name__ == '__main__':
    n = 100000  # Adjust n as needed for your benchmarking purposes
    results = benchmark_sieve(n)
    print("Benchmark results stored in sieve_times.txt")
    
# # Explicitly import required modules
# import sys
# import time

# # Optimized Sieve of Eratosthenes implementation
# def sieve_of_eratosthenes(n):
#     primes = [True] * (n + 1)
#     p = 2
#     while p * p <= n:
#         if primes[p]:
#             for i in range(p * p, n + 1, p):
#                 primes[i] = False
#         p += 1
#     return [p for p in range(2, n + 1) if primes[p]]

# # Measure execution time specifically for Nuitka
# def benchmark_sieve_for_nuitka(n):
#     results = {}
#     log_filename = "sieve_times.txt"  # Log file to store results

#     # Print the current Python version and interpreter
#     print("Running on: {}".format(sys.version))

#     # Check for Nuitka
#     if 'nuitka' in sys.version.lower() or True:  # Ensure this block always runs for Nuitka
#         print("Nuitka block executed")
#         start_time = time.time()
#         sieve_of_eratosthenes(n)
#         end_time = time.time()
#         nuitka_time = end_time - start_time
#         results['Nuitka'] = nuitka_time
#         print("Nuitka - Start: {}, End: {}, Time: {} seconds".format(start_time, end_time, nuitka_time))

#     # Write the results to a text file
#     with open(log_filename, 'a') as log_file:
#         log_file.write("Results for Sieve of Eratosthenes with n={}: \n".format(n))
#         for interpreter, run_time in results.items():
#             log_file.write("{} - Time: {} seconds\n".format(interpreter, run_time))
#         log_file.write("\n")  # Newline for separation between runs

#     return results

# if __name__ == '__main__':
#     n = 100000  # Adjust n as needed for your benchmarking purposes
#     results = benchmark_sieve_for_nuitka(n)
#     print("Benchmark results stored in sieve_times.txt")
