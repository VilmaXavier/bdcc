import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Title of the app
st.title("Assignment Documentation: Algorithm Performance")

# Explanation of the assignment
st.markdown("""
This web app demonstrates the performance comparison between different Python implementations (CPython, PyPy, Jython) for two algorithms: 
1. Fibonacci Sequence 
2. Sieve of Eratosthenes

The algorithms were benchmarked, and results were analyzed for both single-threaded and parallelized executions.
""")

# Section for Algorithm Selection
st.sidebar.header("Select Algorithm for Benchmarking")
algorithm = st.sidebar.radio(
    "Choose an algorithm to view the performance comparison:",
    ("Fibonacci Algorithm", "Sieve of Eratosthenes Algorithm")
)

# Section for Fibonacci Algorithm
if algorithm == "Fibonacci Algorithm":
    st.header("Fibonacci Algorithm")

    # Display a brief explanation of the Fibonacci algorithm
    st.markdown("""
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. 
    We benchmarked this algorithm in both single-threaded and parallelized modes to measure performance.
    """)

    # Display the benchmark result image (graph) for Fibonacci
    st.image("fibonacci_benchmark.png", caption="Fibonacci Algorithm Performance Comparison")

    # Placeholder for time results (to be added)
    st.subheader("Execution Time Results")
    st.image("fibonacci_time_results.png", caption="Fibonacci Time Results")

    # Understanding of the results
    st.subheader("Understanding the Results")
    st.markdown("""
    The performance of the Fibonacci algorithm was evaluated for different values of `n`. The graph compares the execution 
    times of single-threaded and parallelized Fibonacci calculations. From the graph, we can observe the impact of parallelization 
    on reducing execution time for larger values of `n`.

    **Key Observations:**
    - Single-threaded execution shows an exponential increase in execution time as `n` increases.
    - Parallelization helps to significantly reduce the execution time for larger values of `n`, showcasing the effectiveness of parallel processing.
    """)

    # Conclusion for Fibonacci
    st.subheader("Conclusion")
    st.markdown("""
    In conclusion, the Fibonacci algorithm benefits from parallelization when calculating larger values of `n`. The parallel approach 
    provides substantial performance improvements, making it more scalable for higher-order Fibonacci calculations.
    """)

# Section for Sieve of Eratosthenes Algorithm
elif algorithm == "Sieve of Eratosthenes Algorithm":
    st.header("Sieve of Eratosthenes Algorithm")

    # Display a brief explanation of the Sieve of Eratosthenes algorithm
    st.markdown("""
    The Sieve of Eratosthenes is an ancient algorithm used to find all prime numbers up to a given limit `n`. 
    We benchmarked this algorithm in both single-threaded and parallelized modes to analyze performance.
    """)

    # Display the benchmark result image (graph) for Sieve of Eratosthenes
    st.image("sieve_benchmark.png", caption="Sieve of Eratosthenes Algorithm Performance Comparison")

    # Placeholder for time results (to be added)
    st.subheader("Execution Time Results")
    st.image("sieve_time_results.png", caption="Sieve of Eratosthenes Time Results")

    # Understanding of the results
    st.subheader("Understanding the Results")
    st.markdown("""
    The performance of the Sieve of Eratosthenes algorithm was evaluated for different values of `n`. The graph compares 
    the execution times of single-threaded and parallelized implementations. 

    **Key Observations:**
    - Similar to the Fibonacci algorithm, the execution time for single-threaded increases with larger values of `n`.
    - Parallelization significantly reduces the execution time for larger values, making the algorithm more efficient for large-scale prime number calculations.
    """)

    # Conclusion for Sieve of Eratosthenes
    st.subheader("Conclusion")
    st.markdown("""
    The Sieve of Eratosthenes algorithm demonstrates significant performance gains through parallelization. 
    For large `n`, parallel execution offers a much more scalable solution, which is crucial for efficiently handling larger datasets in real-world applications.
    """)

# Further Analysis and Results
st.header("Further Analysis and Results")

st.markdown("""
1. **Performance Comparison**: 
   The results show the time taken for both Fibonacci and Sieve of Eratosthenes algorithms with and without parallelization. 
   
2. **Algorithm Scalability**: 
   The scalability analysis of both algorithms shows how parallelization improves execution time, especially for large input sizes.
""")

