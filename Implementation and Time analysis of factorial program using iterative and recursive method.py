import time

def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n = int(input("Enter a non-negative number: "))

start = time.perf_counter()
result1 = factorial_iterative(n)
end = time.perf_counter()
iterative_time = end - start

start = time.perf_counter()
result2 = factorial_recursive(n)
end = time.perf_counter()
recursive_time = end - start

print("\nIterative Factorial:", result1)
print("Iterative Execution Time:", iterative_time, "seconds")

print("\nRecursive Factorial:", result2)
print("Recursive Execution Time:", recursive_time, "seconds")
