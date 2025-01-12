import streamlit as st
import time
from pathlib import Path

import multiprocessing
import concurrent.futures
import cProfile
import io
import pstats
import matplotlib.pyplot as plt

# ------------------------------- FIBONACCI FUNCTIONS -------------------------------

# Naive Fibonacci (Recursive)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Optimized Fibonacci using dynamic programming
def fibonacci_dynamic(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Worker function for parallel Fibonacci
def fib_worker_task(task_range):
    start, end = task_range
    result = []
    a, b = 0, 1
    for i in range(end):
        if i >= start:
            result.append(a)
        a, b = b, a + b
    return result

# Parallelized Fibonacci Sequence
def parallel_fibonacci(n, workers=2):
    chunk_size = n // workers
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(workers)]
    if ranges[-1][1] < n:
        ranges[-1] = (ranges[-1][0], n)

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(fib_worker_task, ranges))
    return [item for sublist in results for item in sublist]

# ------------------------------- SIEVE OF ERATOSTHENES FUNCTIONS -------------------------------

# Normal Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]

# Worker function for parallel Sieve
def sieve_worker_task(task_range):
    start, end = task_range
    primes = sieve_of_eratosthenes(end)
    return [p for p in primes if p >= start]

# Parallelized Sieve of Eratosthenes
def parallel_sieve(limit, workers=2):
    chunk_size = limit // workers
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(workers)]
    if ranges[-1][1] < limit:
        ranges[-1] = (ranges[-1][0], limit)

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(sieve_worker_task, ranges))
    return [prime for sublist in results for prime in sublist]

# ------------------------------- PERFORMANCE COMPARISON -------------------------------

def run_with_cprofile(func, *args):
    """
    Run a function with cProfile and display the profiling statistics.
    """
    pr = cProfile.Profile()
    pr.enable()
    result = func(*args)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    st.text(s.getvalue())
    return result

def performance_comparison():
    """
    Performance comparison for Fibonacci and Prime Number tasks, with profiling and image display.
    """
    st.header("Performance Comparison")
    task = st.selectbox("Choose the task:", ["Fibonacci Sequence", "Sieve of Eratosthenes"])
    image_folder = Path("images")

    # Set task-specific parameters and images
    if task == "Fibonacci Sequence":
        n = st.number_input("Enter the limit for Fibonacci:", min_value=10, max_value=10000, value=1000)
        image_files = [
            "fibonacci/fibonacci_implementation1.png",
            "fibonacci/fibonacci_implementation2.png",
            "fibonacci/fibonacci_implementation3.png",
            "fibonacci/fibonacci_implementation4.png",
            "fibonacci/fibonacci_implementation5.png"
        ]
        graph_image = "fibonacci/fibo_graph.png"  # Graph for Fibonacci execution time comparison
    else:
        n = st.number_input("Enter the limit for Prime Numbers:", min_value=10, max_value=1000000, value=100000)
        image_files = [
            "sieve/image1.png",
            "sieve/image2.png",
            "sieve/image3.png",
            "sieve/image4.png"
        ]
        graph_image = "sieve/sieve_graph.png"  # Graph for Sieve execution time comparison

    if st.button("Run Test"):
        st.write(f"Running {task}...")
        start = time.time()

        # Run task with profiling
        if task == "Fibonacci Sequence":
            result = run_with_cprofile(fibonacci_dynamic, n)
            st.write(f"Fibonacci Number F({n}) = {result}")
            # Display table of Fibonacci numbers
            st.table({"Index": list(range(n + 1)), "Fibonacci Numbers": [fibonacci_dynamic(i) for i in range(n + 1)]})
        else:
            result = run_with_cprofile(sieve_of_eratosthenes, n)
            st.write(f"Number of primes up to {n}: {len(result)}")
            # Display table of prime numbers
            st.table({"Prime Numbers": result})
        
        end = time.time()
        st.write(f"Execution Time: {end - start:.4f} seconds")

        # Display performance screenshots
        st.write("Performance Screenshots:")
        for img_file in image_files:
            img_path = image_folder / img_file
            if img_path.exists():
                st.image(str(img_path), caption=img_file.split('/')[-1].split('.')[0], width=600)
            else:
                st.warning(f"Image not found: {img_file}")

        # Display the graph comparing execution times
        st.subheader(f"{task} Execution Time Comparison Graph")  # Title above the graph
        graph_path = image_folder / graph_image
        if graph_path.exists():
            st.image(str(graph_path), caption=f"{task} - Execution Time Comparison",width=600)
        else:
            st.warning(f"Graph image not found: {graph_image}")

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
        # Initialize lists to store execution times
        execution_times = []
        worker_counts = [1, workers]
        
        # First, run with one worker (serial execution)
        if task == "Fibonacci Sequence":
            st.write("Running with 1 worker (baseline)...")
            start = time.time()
            result = run_with_cprofile(parallel_fibonacci, n, 1)  # Using 1 worker
            st.write(f"Generated {len(result)} Fibonacci numbers.")
            st.table({"Index": list(range(len(result))), "Fibonacci Numbers": result})
        else:
            st.write("Running with 1 worker (baseline)...")
            start = time.time()
            result = run_with_cprofile(parallel_sieve, n, 1)  # Using 1 worker
            st.write(f"Number of primes found: {len(result)}")
            st.table({"Prime Numbers": result})
        end = time.time()
        exec_time_1_worker = end - start
        st.write(f"Execution Time with 1 worker: {exec_time_1_worker:.4f} seconds")
        execution_times.append(exec_time_1_worker)

        # Now, run with user-selected number of workers
        if task == "Fibonacci Sequence":
            st.write(f"Running with {workers} workers...")
            start = time.time()
            result = run_with_cprofile(parallel_fibonacci, n, workers)
            st.write(f"Generated {len(result)} Fibonacci numbers.")
            st.table({"Index": list(range(len(result))), "Fibonacci Numbers": result})
        else:
            st.write(f"Running with {workers} workers...")
            start = time.time()
            result = run_with_cprofile(parallel_sieve, n, workers)
            st.write(f"Number of primes found: {len(result)}")
            st.table({"Prime Numbers": result})
        end = time.time()
        exec_time_workers = end - start
        st.write(f"Execution Time with {workers} workers: {exec_time_workers:.4f} seconds")
        execution_times.append(exec_time_workers)

        # Plotting the execution times comparison graph
        fig, ax = plt.subplots()
        ax.bar(worker_counts, execution_times, color=['blue', 'green'])
        ax.set_xlabel('Number of Workers')
        ax.set_ylabel('Execution Time (seconds)')
        ax.set_title(f'Execution Time Comparison ({task})')
        st.pyplot(fig)

        # Explanation of why execution time is faster/slower with parallelization
        st.subheader("Why the Execution Time Varies with Parallelization:")
        if exec_time_workers < exec_time_1_worker:
            st.write("""
            With parallelization, the execution time is reduced because the workload is split across multiple workers, allowing them to process different parts of the problem simultaneously. 
            This parallel processing can significantly speed up the overall execution, especially for computationally intensive tasks like Fibonacci or prime number generation.
            However, the effectiveness of parallelization depends on the task, the number of available processors, and the nature of the algorithm being used. In some cases, overhead from task distribution and communication between workers can offset the gains from parallelism.
            """)
        elif exec_time_workers > exec_time_1_worker:
            st.write("""
            In some cases, parallelization might not lead to a speedup. This can happen if the task at hand is not sufficiently complex to benefit from parallel execution, 
            or if the overhead of managing multiple workers exceeds the benefits of parallelism. 
            Tasks like the Fibonacci sequence can sometimes suffer from parallel overhead due to the way they need to be divided and recombined.
            In such cases, running with fewer workers or using a more optimized algorithm may provide better performance.
            """)
        else:
            st.write("""
            In this case, parallelization has not provided any significant speedup, and the execution time remains roughly the same. This could be due to a number of factors, 
            such as low computational complexity of the task or excessive overhead in managing parallel tasks. 
            It highlights the importance of choosing the right algorithm and determining whether parallelization is truly beneficial for a given problem.
            """)

# ------------------------------- BIG O ANALYSIS -------------------------------

def big_o_analysis():
    st.header("Big O Analysis")
    task = st.selectbox("Choose the algorithm:", ["Fibonacci Sequence", "Sieve of Eratosthenes"])
    
    if task == "Fibonacci Sequence":
        st.markdown("""
        *Fibonacci Sequence Complexity*:
        - Recursive Fibonacci: *O(2^n)*
        - Dynamic Programming: *O(n)*
        - Parallelized Version: *O(n / workers)*
        """)
    else:
        st.markdown("""
        *Sieve of Eratosthenes Complexity*:
        - Normal Sieve: *O(n log log n)*
        - Parallelized Sieve: *O(n log log n / workers)*
        """)
    
    n = st.number_input("Enter a number for analysis:", min_value=10, max_value=1000000, value=10000)
    
    if task == "Fibonacci Sequence":
        if st.button("Run Recursive Fibonacci"):
            st.write("Running Recursive Fibonacci...")
            start = time.time()
            run_with_cprofile(fibonacci_recursive, 30)  # Hardcoded smaller n for recursive test
            end = time.time()
            st.write(f"Execution Time (Recursive, O(2^n)): {end - start:.4f} seconds")
        
        if st.button("Run Dynamic Programming Fibonacci"):
            st.write("Running Dynamic Programming Fibonacci...")
            start = time.time()
            run_with_cprofile(fibonacci_dynamic, n)
            end = time.time()
            st.write(f"Execution Time (Dynamic Programming, O(n)): {end - start:.4f} seconds")
    else:
        if st.button("Run Normal Sieve"):
            st.write("Running Normal Sieve...")
            start = time.time()
            run_with_cprofile(sieve_of_eratosthenes, n)
            end = time.time()
            st.write(f"Execution Time (O(n log log n)): {end - start:.4f} seconds")

# ------------------------------- INTRODUCTION PAGE -------------------------------

def introduction_page():
    st.title("Algorithm Performance Evaluation")
    st.markdown("""
    **Welcome to the Algorithm Performance Evaluation App!**

    This app allows you to evaluate and compare the performance of different algorithms with a focus on two primary algorithms:
    - **Fibonacci Sequence** (Recursive, Dynamic Programming, and Parallelized versions)
    - **Sieve of Eratosthenes** (Normal and Parallelized versions)

    The app provides insights into:
    - **Performance Comparison**: Compare execution times for different versions of algorithms.
    - **Parallelization**: Test the impact of parallel processing on algorithm execution time.
    - **Big O Analysis**: Understand the theoretical time complexity of the algorithms.

    ## Pages in this app:

    1. **Introduction**: A brief overview of the app and its functionalities (You are here now).
    2. **Performance Comparison**: Compare the performance of the Fibonacci sequence and the Sieve of Eratosthenes algorithms in terms of execution time.
    3. **Parallelization**: Explore how parallel execution affects performance for both algorithms and compare execution times with different numbers of workers.
    4. **Big O Analysis**: A theoretical analysis of the time complexity of the Fibonacci and Sieve of Eratosthenes algorithms, both in their normal and parallelized forms.

    Use the sidebar to navigate between the different sections of the app. Each section is designed to give you a deeper understanding of algorithmic performance, parallelization, and time complexity.
    """)

# ------------------------------- MAIN APP LAYOUT -------------------------------

# Sidebar with names and roll numbers alongside page navigation
page = st.sidebar.radio(
    "Select a Page",
    ["Introduction", "Performance Comparison", "Parallelization", "Big O Analysis"],
)

# Add a bold and larger font display of names and roll numbers on the sidebar
st.sidebar.markdown("<h3 style='text-align: center; font-size: 22px; font-weight: bold;'>Created by:</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='text-align: center; font-size: 20px; font-weight: bold;'>Alethea Tamanna (Roll No: 15)</h4>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='text-align: center; font-size: 20px; font-weight: bold;'>Vilma Xavier (Roll No: 16)</h4>", unsafe_allow_html=True)

# Display the selected page content
if page == "Introduction":
    introduction_page()
elif page == "Performance Comparison":
    performance_comparison()
elif page == "Parallelization":
    parallelization_section()
elif page == "Big O Analysis":
    big_o_analysis()
