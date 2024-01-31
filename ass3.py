

##matrix transpose1
x=[[2,4],
   [6,8],
   [12,7]]
result=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i]=x[i][j]
    for r in result:
        print(r)

        ##2
lines = []
while True:
    line = input("Enter a line (or type 'done' to finish): ")
    if line.lower() == 'done':
        break
    lines.append(line)

# Capitalizing each line and printing the result
print("\nCapitalized Lines:")
for line in lines:
    print(line.upper())

## build in fun of list3
        
x=["anu",3,"vinu",1,5,"ammu"]
print(x[2])
y=x[1:3]
print(y)
z=x+y
print(z)
x.append(9)
print(x)
x.insert(2,"anju")
print(x)
x.remove("vinu")
print(x)
x.pop(3)
print(x)
ind=x.index("anju")
print(ind)
repeatlist=y*2
print(repeatlist)
length=len(z)
print(length)


##4
def read_dictionary():
    dictionary = {}
    while True:
        key = input("Enter a key (or type 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input("Enter the corresponding value: ")
        dictionary[key] = value
    return dictionary

# Read the first dictionary
print("Enter values for the first dictionary:")
dict1 = read_dictionary()

# Read the second dictionary
print("\nEnter values for the second dictionary:")
dict2 = read_dictionary()

# Merge the dictionaries
merged_dict = {**dict1, **dict2}

# Print the merged dictionary
print("\nMerged Dictionary:")
print(merged_dict)

##5
# Creating a sample dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York', 'salary': 50000}

# 1. get(key, default=None)
print("1. get('age'):", my_dict.get('age'))

# 2. keys()
print("2. keys():", my_dict.keys())

# 3. values()
print("3. values():", my_dict.values())

# 4. items()
print("4. items():", my_dict.items())

# 5. update()
my_dict.update({'city': 'San Francisco', 'department': 'IT'})
print("5. update():", my_dict)

# 6. pop(key)
age = my_dict.pop('age')
print("6. pop('age'):", age)
print("   Dictionary after pop:", my_dict)

# 7. popitem()
last_item = my_dict.popitem()
print("7. popitem():", last_item)
print("   Dictionary after popitem:", my_dict)

# 8. clear()
my_dict.clear()
print("8. clear():", my_dict)

# 9. fromkeys(seq, value=None)
keys = ['name', 'age', 'city']
default_value = 'Not Available'
new_dict = dict.fromkeys(keys, default_value)
print("9. fromkeys():", new_dict)

# 10. copy()
original_dict = {'a': 1, 'b': 2}
copied_dict = original_dict.copy()
print("10. copy():", copied_dict)

# 11. setdefault(key, default=None)
original_dict.setdefault('c', 3)
print("11. setdefault('c', 3):", original_dict)

# 12. len()
print("12. len():", len(original_dict))

# 13. in
print("13. 'a' in original_dict:", 'a' in original_dict)

# 14. clear()
original_dict.clear()
print("14. clear():", original_dict)

##6
##sum of list
def calculate_sum(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

my_list = [1, 2, 3, 4, 5]
result = calculate_sum(my_list)
print(f"The sum of elements in the list is: {result}")


##7
def generate_square_dictionary(n):
    square_dict = {i: i*i for i in range(1, n + 1)}
    return square_dict

# Get user input for n
n = int(input("Enter an integral number (n): "))

# Generate and print the dictionary
result_dict = generate_square_dictionary(n)
print("Generated Dictionary:", result_dict)

##8
sentence = input("Enter a sentence: ")

# Initialize counters for letters and digits
letter_count = 0
digit_count = 0

# Iterate through each character in the sentence
for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

# Print the results
print("Number of letters:", letter_count)
print("Number of digits:", digit_count)


##9


def is_even(num):
    return num % 2 == 0

# Function for map(): Square each number
def square(num):
    return num ** 2

# Function for reduce(): Calculate the product of all numbers
def multiply(x, y):
    return x * y

# Use filter() to get even numbers
even_numbers = list(filter(is_even, numbers))
print("Filtered (Even Numbers):", even_numbers)

# Use map() to square each number
squared_numbers = list(map(square, numbers))
print("Mapped (Squared Numbers):", squared_numbers)

# Use reduce() to calculate the product of all numbers
product_of_numbers = reduce(multiply, numbers)
print("Reduced (Product of Numbers):", product_of_numbers)

##10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Example 2 - Even Numbers:", even_numbers)


###11
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num**2 for num in numbers}

# Display the original list and the created dictionary
print("Original List:", numbers)
print("Dictionary of Squares:", squares_dict)

##12

def find_largest_smallest(numbers):
    if not numbers:
        return None, None  # Return None for both largest and smallest if the list is empty

    # Initialize variables for the largest and smallest elements
    largest = smallest = numbers[0]

    # Iterate through the list to find the largest and smallest elements
    for num in numbers:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest

# Example usage:
my_list = [12, 45, 78, 34, 21, 56, 89, 9, 3, 67]

largest, smallest = find_largest_smallest(my_list)

print("List:", my_list)
print("Largest Element:", largest)
print("Smallest Element:", smallest)

##13


def remove_even_numbers(numbers):
    # Use filter to keep only odd numbers in the list
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    return odd_numbers

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = remove_even_numbers(my_list)

print("Original List:", my_list)
print("List after removing even numbers:", result)


##14
def generate_square_list(start, end):
    # Generate a list of squares of numbers between start and end
    square_list = [num**2 for num in range(start, end + 1)]
    return square_list

# Example usage:
start_value = 1
end_value = 30

square_list = generate_square_list(start_value, end_value)

# Print the first and last 5 elements
print("Generated List of Squares:")
print("First 5 elements:", square_list[:5])
print("Last 5 elements:", square_list[-5:])


##15
def insert_string_at_beginning(string, my_list):
    # Use list comprehension to insert the string at the beginning of each item
    updated_list = [string + str(item) for item in my_list]
    return updated_list

# Example usage:
given_string = "Prefix"
original_list = [1, 2, 3, 4, 5]

result_list = insert_string_at_beginning(given_string, original_list)

# Print the original and updated lists
print("Original List:", original_list)
print(f"List after inserting '{given_string}' at the beginning:", result_list)


##16
def iterate_over_two_lists(list1, list2):
    # Use zip to iterate over two lists simultaneously
    for item1, item2 in zip(list1, list2):
        print(item1, item2)

# Example usage:
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

iterate_over_two_lists(list1, list2)

##17

def add_key_to_dict(my_dict, key, value):
    # Use the square bracket notation to add a key-value pair to the dictionary
    my_dict[key] = value
    return my_dict

# Example usage:
original_dict = {'a': 1, 'b': 2, 'c': 3}
new_key = 'd'
new_value = 4

updated_dict = add_key_to_dict(original_dict, new_key, new_value)

# Print the original and updated dictionaries
print("Original Dictionary:", original_dict)
print("Updated Dictionary:", updated_dict)

##18

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries
concatenated_dict = {**dic1, **dic2, **dic3}

# Print the concatenated dictionary
print("Concatenated Dictionary:", concatenated_dict)

##19

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterate over key-value pairs
print("Key-Value Pairs:")
for key, value in my_dict.items():
    print(key, value)my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterate over key-value pairs
print("Key-Value Pairs:")
for key, value in my_dict.items():
    print(key, value)

    ##20

my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Sum all the values in the dictionary
total_sum = sum(my_dict.values())

# Print the result
print("Sum of all items in the dictionary:", total_sum)

##21

pet_dict = {'Dog': 'Willie', 'Cat': 'Mittens', 'Parrot': 'Polly'}

# Iterate over the dictionary and print statements
for animal, name in pet_dict.items():
    print(f"{name} is a {animal}.")

##22
    
def filter_subjects_above_50(marks):
    # Use dictionary comprehension to create a new dictionary with marks more than 50
    new_marks = {subject: mark for subject, mark in marks.items() if mark > 50}
    return new_marks

# Given dictionary
marks = {'English': 40, 'Maths': 60, 'Hindi': 30, 'Chemistry': 46, 'Physics': 70}

# Call the function to filter subjects with marks more than 50
filtered_marks = filter_subjects_above_50(marks)

# Print the original and filtered dictionaries
print("Original Dictionary:", marks)
print("Filtered Dictionary (Subjects with Marks > 50):", filtered_marks)    

##23
def count_letters_and_digits(sentence):
    result = {'letters': 0, 'digits': 0}

    for char in sentence:
        if char.isalpha():
            result['letters'] += 1
        elif char.isdigit():
            result['digits'] += 1

    return result

# Example usage:
sentence = "Hello123 World!"
result_dict = count_letters_and_digits(sentence)
print(result_dict)

##24
def generate_square_dictionary(n):
    # Use dictionary comprehension to create a dictionary with keys and their squares
    square_dict = {num: num**2 for num in range(1, n + 1)}
    return square_dict

# Example usage:
n_value = 5  # You can change this value to generate a dictionary for a different range

result_dict = generate_square_dictionary(n_value)

# Print the generated dictionary
print(f"Generated Dictionary (Keys: 1 to {n_value}, Values: Squares):")
print(result_dict)