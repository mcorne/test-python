# Generated then optimized by CodeIgniter from the following instructions:
# Write a Python program to find the two largest numbers between 1 and 999
# whose product is a palindrome, and display these numbers, the palindrome,
# the number of iterations, and the processing time.

import time


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def find_largest_palindrome(max):
    start_time = time.time()
    max_palindrome = 0
    num1 = 0
    num2 = 0
    iterations = 0

    for i in range(max, 100, -1):
        if i * max < max_palindrome:
            break  # If the maximum possible product is less than the largest palindrome found, stop the outer loop
        for j in range(i, 100, -1):
            iterations += 1
            product = i * j
            if product <= max_palindrome:
                break  # Stop the inner loop if the product is less than the largest palindrome found
            if is_palindrome(product):
                max_palindrome = product
                num1 = i
                num2 = j

    end_time = time.time()
    elapsed_time = end_time - start_time

    return num1, num2, max_palindrome, iterations, elapsed_time


n1, n2, palindrome, iterations, elapsed_time = find_largest_palindrome(999)

print(f"The two numbers are: {n1} and {n2}")
print(f"The palindrome is: {palindrome}")
print(f"Number of iterations: {iterations}")
print(f"Processing time: {elapsed_time:.6f} seconds")
