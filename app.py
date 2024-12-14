import streamlit as st
import time
import multiprocessing
import concurrent.futures
import numpy as np

def intro():
    st.title("Python Flavors, Parallelization, and Big O Scaling")
    st.markdown("""
    ## Part 1: Python Flavors
    Python has several implementations or flavors, each optimized for different use cases:
    - **CPython**: The default implementation, known for its extensive library support.
    - **PyPy**: Focused on performance, featuring a Just-In-Time (JIT) compiler.
    - **Jython**: Python for the Java Virtual Machine (JVM).
    - **IronPython**: Python for the .NET framework.

    ### Performance Bridge
    PyPy often offers better performance for CPU-bound tasks because of its JIT compiler, whereas CPython is better for compatibility.

    ### Experiment with Complex Programs
    Below, you can test the performance of a complex CPU-bound program.
    """)

# Function to simulate a CPU-bound task
def cpu_bound_task(n):
    total = 0
    for i in range(1, n):
        total += i * i
    return total

def part1():
    st.header("Part 1: Performance Comparison")
    n = st.number_input("Enter the range for computation (higher values increase complexity):", min_value=10000, max_value=10000000, value=100000)
    if st.button("Run Test"):
        st.write("Running task...")
        start = time.time()
        cpu_bound_task(n)
        end = time.time()
        st.write(f"Execution Time with CPython: {end - start:.4f} seconds")
        st.markdown("Try PyPy for a comparison.")


def part2():
    st.header("Part 2: Parallelization of Algorithms")
    st.markdown("""
    Parallelization can significantly improve performance, especially for CPU-bound tasks.
    """)

    def parallel_task(n):
        total = 0
        for i in range(n):
            total += i * i
        return total

    n = st.number_input("Enter the range for computation in parallel (higher values increase complexity):", min_value=10000, max_value=10000000, value=100000)
    workers = st.slider("Select the number of parallel workers:", 1, multiprocessing.cpu_count(), 2)

    if st.button("Run Parallel Test"):
        st.write("Running parallel task...")
        data = [n // workers for _ in range(workers)]

        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(parallel_task, data)
        end = time.time()

        st.write(f"Execution Time with {workers} workers: {end - start:.4f} seconds")


def part3():
    st.header("Part 3: Big O Notation and Parallelization")
    st.markdown("""
    ### Does Big O Notation Scale with Parallelization?
    - Big O measures the asymptotic complexity of an algorithm, not actual performance.
    - Parallelization can reduce the constants in execution time but doesn't change the fundamental Big O.

    For example:
    - An $O(n^2)$ algorithm remains $O(n^2)$ even if parallelized, though the actual runtime may reduce.
    - Test this below.
    """)

    def quadratic_algorithm(data):
        results = []
        for i in data:
            for j in data:
                results.append(i * j)
        return results

    n = st.number_input("Enter the size of the dataset (higher values increase complexity):", min_value=10, max_value=500, value=50)
    data = np.arange(n)

    if st.button("Run Quadratic Algorithm"):
        st.write("Running algorithm...")
        start = time.time()
        quadratic_algorithm(data)
        end = time.time()

        st.write(f"Execution Time (O(n^2)): {end - start:.4f} seconds")

# Streamlit App Layout
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Introduction", "Part 1", "Part 2", "Part 3"])

if page == "Introduction":
    intro()
elif page == "Part 1":
    part1()
elif page == "Part 2":
    part2()
elif page == "Part 3":
    part3()
