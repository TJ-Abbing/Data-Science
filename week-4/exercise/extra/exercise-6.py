"""
Exercises 6:
Write a function that generates a string of fibonaci number up to the given number as argument.
If you do not know what a fibonaci sequence is, check this Wikipedia link:
https://en.wikipedia.org/wiki/Fibonacci_sequence
Make sure that your function returns this error message if the argument is less than zero: "Invalid input. n must be a positive integer".
The string should contain all the fibonaci numbers with a space between each number.
"""

def fibonaci(n):
    if n < 0:
        return "Invalid input. n must be a positive integer."
    
    if n == 0:
        return "0"
    
    if n == 1:
        return "0 1"
    
    fibonaci_string = "0 1"
    fibonaci_num = 1
    fibonaci_num_prev = 0
    for i in range(2, n+1):
        fibonaci_num_new = fibonaci_num + fibonaci_num_prev
        fibonaci_num_prev = fibonaci_num
        fibonaci_num = fibonaci_num_new
        fibonaci_string += f" {fibonaci_num}"
    
    return fibonaci_string

# Test the function
n = int(input("Enter a number: "))
fibonaci_string = fibonaci(n)
print(f"The fibonaci sequence up to {n} is: {fibonaci_string}.")