import streamlit as st
import time
import multiprocessing
import concurrent.futures
from pathlib import Path

# ------------------------------- FIBONACCI FUNCTIONS -------------------------------

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_dynamic(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

def fib_worker_task(task_range):
    start, end = task_range
    result = []
    a, b = 0, 1
    for i in range(end):
        if i >= start:
            result.append(a)
        a, b = b, a + b
    return result

def parallel_fibonacci(n, workers=2):
    chunk_size = n // workers
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(workers)]
    if ranges[-1][1] < n:
        ranges[-1] = (ranges[-1][0], n)

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(fib_worker_task, ranges))
    return [item for sublist in results for item in sublist]

# ------------------------------- SIEVE OF ERATOSTHENES FUNCTIONS -------------------------------

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]

def sieve_worker_task(task_range):
    start, end = task_range
    primes = sieve_of_eratosthenes(end)
    return [p for p in primes if p >= start]

def parallel_sieve(limit, workers=2):
    chunk_size = limit // workers
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(workers)]
    if ranges[-1][1] < limit:
        ranges[-1] = (ranges[-1][0], limit)

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(sieve_worker_task, ranges))
    return [prime for sublist in results for prime in sublist]

# ------------------------------- PERFORMANCE COMPARISON -------------------------------

def performance_comparison():
    st.header("Performance Comparison")
    task = st.selectbox("Choose the task:", ["Fibonacci Sequence", "Sieve of Eratosthenes"])
    image_folder = Path("bdcc/images")

    if task == "Fibonacci Sequence":
        n = st.number_input("Enter the limit for Fibonacci:", min_value=10, max_value=10000, value=1000)
        image_files = [
            "fibonacci/fibonacci_implementation1.png",
            "fibonacci/fibonacci_implementation2.png",
            "fibonacci/fibonacci_implementation3.png",
            "fibonacci/fibonacci_implementation4.png",
            "fibonacci/fibonacci_implementation5.png"
        ]
    else:
        n = st.number_input("Enter the limit for Prime Numbers:", min_value=10, max_value=1000000, value=100000)
        image_files = [
            "sieve/image1.png",
            "sieve/image2.png",
            "sieve/image3.png",
            "sieve/image4.png"
        ]

    if st.button("Run Test"):
        st.write(f"Running {task}...")
        start = time.time()

        if task == "Fibonacci Sequence":
            result = fibonacci_dynamic(n)
            st.write(f"Fibonacci Number F({n}) = {result}")
        else:
            result = sieve_of_eratosthenes(n)
            st.write(f"Number of primes up to {n}: {len(result)}")
        
        end = time.time()
        st.write(f"Execution Time: {end - start:.4f} seconds")
        
        # Display images
        st.write("Performance Screenshots:")
        for img_file in image_files:
            img_path = image_folder / img_file
            st.write(f"Looking for image: {img_path}")  # Debugging output
            if img_path.exists():
                st.image(str(img_path), caption=img_file.split('/')[-1].split('.')[0], use_column_width=True)
            else:
                st.warning(f"Image not found: {img_file}")

# ------------------------------- PARALLELIZATION SECTION -------------------------------

def parallelization_section():
    st.header("Parallelization")
    task = st.selectbox("Choose the algorithm:", ["Fibonacci Sequence", "Sieve of Eratosthenes"])
    
    if task == "Fibonacci Sequence":
        n = st.number_input("Enter the limit for Fibonacci:", min_value=10, max_value=10000, value=1000)
    else:
        n = st.number_input("Enter the limit for Prime Numbers:", min_value=10, max_value=1000000, value=100000)

    workers = st.slider("Select the number of parallel workers:", 1, multiprocessing.cpu_count(), 2)

    if st.button("Run Parallel Test"):
        start = time.time()
        
        if task == "Fibonacci Sequence":
            result = parallel_fibonacci(n, workers)
            st.write(f"Generated {len(result)} Fibonacci numbers.")
        else:
            result = parallel_sieve(n, workers)
            st.write(f"Number of primes found: {len(result)}")
        
        end = time.time()
        st.write(f"Execution Time with {workers} workers: {end - start:.4f} seconds")

# ------------------------------- BIG O ANALYSIS -------------------------------

def big_o_analysis():
    st.header("Big O Analysis")
    task = st.selectbox("Choose the algorithm:", ["Fibonacci Sequence", "Sieve of Eratosthenes"])
    
    if task == "Fibonacci Sequence":
        st.markdown("""        
        **Fibonacci Sequence Complexity**:
        - Recursive Fibonacci: **O(2^n)**
        - Dynamic Programming: **O(n)**
        - Parallelized Version: **O(n / workers)**
        """)
    else:
        st.markdown("""        
        **Sieve of Eratosthenes Complexity**:
        - Normal Sieve: **O(n log log n)**
        - Parallelized Sieve: **O(n log log n / workers)**
        """)

    n = st.number_input("Enter a number for analysis:", min_value=10, max_value=1000000, value=10000)
    
    if task == "Fibonacci Sequence":
        if st.button("Run Recursive Fibonacci"):
            st.write("Running Recursive Fibonacci...")
            start = time.time()
            fibonacci_recursive(30)  # Hardcoded smaller n for recursive test
            end = time.time()
            st.write(f"Execution Time (Recursive, O(2^n)): {end - start:.4f} seconds")
        
        if st.button("Run Dynamic Programming Fibonacci"):
            st.write("Running Dynamic Programming Fibonacci...")
            start = time.time()
            fibonacci_dynamic(n)
            end = time.time()
            st.write(f"Execution Time (Dynamic Programming, O(n)): {end - start:.4f} seconds")
    else:
        if st.button("Run Normal Sieve"):
            st.write("Running Normal Sieve...")
            start = time.time()
            sieve_of_eratosthenes(n)
            end = time.time()
            st.write(f"Execution Time (O(n log log n)): {end - start:.4f} seconds")

# ------------------------------- STREAMLIT APP LAYOUT -------------------------------

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Introduction", "Performance Comparison", "Parallelization", "Big O Analysis"])

if page == "Introduction":
    st.title("Algorithm Performance Evaluation")
    st.markdown("""
    This application compares the performance of different algorithms:
    - **Fibonacci Sequence** (Recursive, Dynamic Programming, and Parallelized versions)
    - **Sieve of Eratosthenes** (Normal and Parallelized versions)
    """)
elif page == "Performance Comparison":
    performance_comparison()
elif page == "Parallelization":
    parallelization_section()
elif page == "Big O Analysis":
    big_o_analysis()
