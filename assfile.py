



# # Reading the content of the file
# with open('exampl1.txt', 'r') as file:
#     content_before = file.read()
#     print("Content before writing:")
#     print(content_before)

# # Writing new content to the file
# with open('exampl1.txt', 'w') as file:
#     file.write("hello\n")
#     file.write("i am fazi\n")
#     file.write("i am an Indian\n")

# # Reading and printing the updated content of the file
# with open('exampl1.txt', 'r') as file:
#     content_after = file.read()
#     print("\nContent after writing:")
#     print(content_after)

# with open('exampl1.txt','r')as file:
#     # readl=file.read()
#     # print(readl)
#     # readll=file.readline()
#     # print(readll)
#     # readl3=file.readlines()
#     # print(readl3)

# ##solve quadratic equation
#     import cmath  # Import the complex math module for handling complex roots

# def solve_quadratic_equation(a, b, c):
#     # Calculate the discriminant
#     delta = cmath.sqrt(b**2 - 4*a*c)

#     # Calculate the roots using the quadratic formula
#     root1 = (-b + delta) / (2 * a)
#     root2 = (-b - delta) / (2 * a)

#     return root1, root2

# # Example usage
# a = 1
# b = -3
# c = 2

# roots = solve_quadratic_equation(a, b, c)
# print(f"The roots are: {roots}")

# ##read write in csv

# import csv

# # Function to write data to a CSV file
# def write_to_csv(file_name, data):
#     with open(file_name, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         # Write header
#         writer.writerow(["Name", "Age", "City"])
#         # Write data
#         for row in data:
#             writer.writerow(row)

# # Function to read data from a CSV file
# def read_from_csv(file_name):
#     data = []
#     with open(file_name, mode='r') as file:
#         reader = csv.reader(file)
#         # Skip header
#         next(reader)
#         # Read data
#         for row in reader:
#             data.append(row)
#     return data

# # Example usage
# file_name = "example.csv"

# # Write data to CSV
# data_to_write = [
#     ["John", "25", "New York"],
#     ["Jane", "30", "London"],
#     ["Bob", "22", "San Francisco"]
# ]

# write_to_csv(file_name, data_to_write)
# print(f"Data written to {file_name}")

# # Read data from CSV
# data_read = read_from_csv(file_name)
# print("Data read from CSV:")
# for row in data_read:
#     print(row)

##append
# Example usage for appending to a normal text file
file_name = "example.txt"

# Data to append
data_to_append = [
    "New line 1",
    "New line 2"
]

# Append data to existing file
with open(file_name, mode='a') as file:
    # Write data
    for line in data_to_append:
        file.write(line + '\n')  # Adding a newline after each line

print(f"Data appended to {file_name}")

# Read data from the updated file
with open(file_name, mode='r') as file:
    print("Updated data:")
    for line in file:
        print(line.strip())  # Removing newline characters for display
