import time

class FastFibonacci:
    """
    A class to calculate Fibonacci numbers using two approaches:
    1. Standard recursive method (inefficient for large n).
    2. Optimized recursive method with memoization (efficient for large n).
    
    Attributes:
        memo (dict): A dictionary to store precomputed Fibonacci values for optimization.
    """

    def __init__(self):
        """
        Initializes a FastFibonacci instance with an empty memoization dictionary.
        """
        self.memo = {}

    def fibonacci(self, n):
        """
        Computes the nth Fibonacci number using standard recursion.
        
        This method is highly inefficient for large values of n due to exponential 
        growth in the number of recursive calls (O(2^n)).

        Args:
            n (int): The position of the Fibonacci number to compute.

        Returns:
            int: The nth Fibonacci number.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fast_fibonacci(self, n):
        """
        Computes the nth Fibonacci number using memoization.
        
        Memoization stores the results of previously computed Fibonacci numbers, 
        drastically reducing redundant calculations and improving time complexity 
        to O(n).

        Args:
            n (int): The position of the Fibonacci number to compute.

        Returns:
            int: The nth Fibonacci number.
        """
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        self.memo[n] = self.fast_fibonacci(n - 1) + self.fast_fibonacci(n - 2)
        return self.memo[n]

    def reset_memo(self):
        """
        Resets the memoization dictionary.

        This method is useful when you want to compute Fibonacci numbers for 
        new inputs without retaining previous computations.
        """
        self.memo = {}

# Example usage
n = 36
ff = FastFibonacci()

# Standard Recursive Fibonacci
# Time Complexity: O(2^n), Space Complexity: O(n) (due to recursion stack)
start_time = time.time()
fib = ff.fibonacci(n)
end_time = time.time()
print(f"Fibonacci({n}) without memoization: {fib} (Time taken: {end_time - start_time:.4f} seconds)")

# Optimized Fibonacci with Memoization
# Time Complexity: O(n), Space Complexity: O(n) (due to memo dictionary and recursion stack)
ff.reset_memo()  # Ensure memo is reset before new computation
start_time = time.time()
ffib = ff.fast_fibonacci(n)
end_time = time.time()
print(f"Fibonacci({n}) with memoization: {ffib} (Time taken: {end_time - start_time:.4f} seconds)")

# Expected Output:
# Fibonacci(36) without memoization: 14930352 (Time taken: 9.8407 seconds)
# Fibonacci(36) with memoization: 14930352 (Time taken: 0.0000 seconds)
