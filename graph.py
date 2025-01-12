import matplotlib.pyplot as plt

# Updated data for Fibonacci execution times (n=35)
fibo_environments = ['PyPy', 'CPython', 'Nuitka', 'Anaconda']
fibo_times = [1.1444091796875e-05, 2.1457672119140625e-06, 4.0531158447265625e-06, 2.1457672119140625e-06]

# Data for Sieve execution times
sieve_environments = ['PyPy', 'CPython', 'Anaconda', 'Nuitka']
sieve_times = [0.0029091835021972656, 0.006265163421630859, 0.0051004886627197266, 0.00568389892578125]

def create_fibo_graph():
    """Creates and saves the Fibonacci execution time graph."""
    plt.figure(figsize=(8, 6))
    plt.bar(fibo_environments, fibo_times, color=['red', 'green', 'blue', 'orange'])
    plt.title('Fibonacci Execution Time Comparison (n=35)', fontsize=14)
    plt.xlabel('Environment', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.tight_layout()
    plt.savefig("fibo_graph.png")  # Save as an image file
    plt.close()  # Close the plot to avoid overlap with other graphs

def create_sieve_graph():
    """Creates and saves the Sieve of Eratosthenes execution time graph."""
    plt.figure(figsize=(8, 6))
    plt.bar(sieve_environments, sieve_times, color=['red', 'green', 'orange', 'blue'])
    plt.title('Sieve of Eratosthenes Execution Time Comparison (n=100000)', fontsize=14)
    plt.xlabel('Environment', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.tight_layout()
    plt.savefig("sieve_graph.png")  # Save as an image file
    plt.close()  # Close the plot to avoid overlap with other graphs

if __name__ == "__main__":
    create_fibo_graph()  # Create Fibonacci graph
    create_sieve_graph()  # Create Sieve graph
    print("Graphs have been saved as 'fibo_graph.png' and 'sieve_graph.png'.")
