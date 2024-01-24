##odd or even

def check_even_odd(number):
    if number % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")

# Example usage:
user_input = int(input("Enter an integer: "))
check_even_odd(user_input)

##generate dictionary

def generate_square_dictionary(n):
    square_dict = {}
    for i in range(1, n + 1):
        square_dict[i] = i * i
    return square_dict

number = int(input("Enter a number (n): "))
result_dict = generate_square_dictionary(number)

print("Generated Dictionary:")
print(result_dict)

##count lettters in string
def count_letters_and_digits(sentence):
    letters_count = 0
    digits_count = 0

    for char in sentence:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1

    return letters_count, digits_count

user_sentence = input("Enter a sentence: ")
letters, digits = count_letters_and_digits(user_sentence)

print(f"Number of letters: {letters}")
print(f"Number of digits: {digits}")

###filter map

umbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def custom_filter(func, iterable):
    return [item for item in iterable if func(item)]


filtered_numbers = custom_filter(lambda x: x % 2 == 0, numbers)
print("Filtered even numbers:", filtered_numbers)


def custom_map(func, iterable):
    return [func(item) for item in iterable]

squared_numbers = custom_map(lambda x: x ** 2, numbers)
print("Squared numbers:", squared_numbers)

def custom_reduce(func, iterable, initial=None):
    iterator = iter(iterable)
    if initial is None:
        result = next(iterator)
    else:
        result = initial
    for item in iterator:
        result = func(result, item)
    return result


product_of_numbers = custom_reduce(lambda x, y: x * y, numbers, 1)
print("Product of all numbers:", product_of_numbers)


##remove vowe
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result_string = ''.join([char for char in input_string if char not in vowels])
    return result_string
user_input = input("Enter a string: ")
result = remove_vowels(user_input)
print("String with vowels removed:", result)

##power using lambda map
num_powers = 5
powers_of_2 = map(lambda x: 2 ** x, range(num_powers))

print("Powers of 2:", list(powers_of_2))

##list int dic

def create_dictionary(keys, values):
    # Check if the lists have the same length
    if len(keys) != len(values):
        raise ValueError("Lists must have the same length")

    # Use zip to combine the lists and create a dictionary
    result_dict = dict(zip(keys, values))
    return result_dict

# Example usage:
keys_list = ["a", "b", "c", "d"]
values_list = [1, 2, 3, 4]

result_dictionary = create_dictionary(keys_list, values_list)
print("Resulting Dictionary:", result_dictionary)

##fib using recursion
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
num_terms = int(input("Enter the number of Fibonacci terms: "))
fibonacci_series = fibonacci_recursive(num_terms)
print("Fibonacci Series:", fibonacci_series)

##fact using rec

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
number = int(input("Enter a number to find its factorial: "))
result = factorial_recursive(number)
print(f"The factorial of {number} is: {result}")

##dec time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        import timeit
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        elapsed_time = end_time - start_time
        print(f"Time taken to execute {func.__name__}: {elapsed_time:.6f} seconds")
        return result
    return wrapper


@timing_decorator
def sample_function():
   
    import time
    time.sleep(2)
    print("Function executed")

sample_function()

##generator

def generate_numbers(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num
n = int(input("Enter a value for n: "))
result_generator = generate_numbers(n)
result_str = ', '.join(map(str, result_generator))
print(f"Numbers divisible by 5 and 7 between 0 and {n}: {result_str}")

##gen even

def generate_even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

n = int(input("Enter a value for n: "))
result_generator = generate_even_numbers(n)
result_str = ', '.join(map(str, result_generator))
print(f"Even numbers between 0 and {n}: {result_str}")

##
def find_second_smallest(numbers):
    if len(numbers) < 2:
        return "List must have at least two elements."
    smallest = min(numbers)
    second_smallest = min(num for num in numbers if num != smallest)

    return second_smallest

num_list = [12, 5, 8, 2, 15, 7, 6]
result = find_second_smallest(num_list)

print(f"The second smallest number in the list {num_list} is: {result}")