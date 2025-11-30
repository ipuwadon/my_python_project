def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        print(f"from factorial_iter i = {i}, n = {n}, result = {result}")
    return result

def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    # Debug print (optional)
    # print(f"from factorial_rec n = {n}")
    return n * factorial_rec(n-1)

print(factorial_iter(5))   # Output: 120
print(factorial_rec(5))    # Output: 120