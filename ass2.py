##1check even or odd

x=5
if(x % 2 == 0):
    print(x," is even number")
else:
    print(x," odd number")

    ##2 swap two variables

    x=10
    y=20
    print("x = ",x)
    print("y = ",y)
    print("after swap")
    temp=x
    x=y
    y=temp
    print("x = ",x)
    print("y = ",y)


##3 positive or negative
    
x=0
if(x > 0):
    print("x is positive")
elif(x < 0):
    print("x is negative")
else:
    print("x is 0")

##4 fibinocci series
    
    n=10
    fbseries=[0,1]
    while len(fbseries) < n:
        fbseries.append(fbseries[-1]+fbseries[-2])
    print(fbseries)

    ##patterns
    ##a

n=6
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()


##prime numbers
    
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Find and print prime numbers between 1 and 10
for num in range(1, 11):
    if is_prime(num):
        print(num, end=" ")


##odd and sum
sum=0        
for x in range(1,51):
    if(x % 2 != 0):
        print(x,end=" ")
        sum=sum+x
print("sum is  ",sum)

##factorial

num=5
fact=1
count=1
while count <= num:
    fact*=count
    count+=1
print("factorial of ",num ," ", "is",fact)

##palliandrome

str1="malayalam"
str1 = str1.replace(" ", "")
if(str1 == str1[::-1]):
    print(str1+" paliandrome")
else:
    print(str1+" not paliandrome")

##sum between 100 and 200
sum=0   
for x in range(101,200):
    sum=sum+x
print("sum is ",sum)

##multiplication table

num=3
limit=10
for i in range(1,limit+1):
    result= num*i
    print(result)

##area perimeter
    
l = 10
b=6
a = l*b
print("area is  ",a)
p= 2*(l+b)
print("perimeter is ",p)

##sum of n natural number

n=10
sum=0
for i in range(1,11):
    sum=sum+i
print("sum is  ",sum)

##amstrong number

def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num

# Example: 153 is an Armstrong number
example_number = 153

if is_armstrong_number(example_number):
    print(f"{example_number} is an Armstrong number.")
else:
    print(f"{example_number} is not an Armstrong number.")

#largest

a=7
b=5
c=56
if(a>b & a>c):
    print("largest is a  ",a)
elif(b>a & b>c):
    print("b is greater",b)
else:
    print("largest is c  ",c)

    ##remove punc

def remove_punctuation(input_string):
    
    punctuation_set = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    
    result_string = ''.join(char for char in input_string if char not in punctuation_set)

    return result_string


input_string = "Hello, world! This is an example string with punctuations!!!"
cleaned_string = remove_punctuation(input_string)

print("Original string:", input_string)
print("String without punctuations:", cleaned_string)

##pattern
def display_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# Example usage
num_rows = 5  
display_triangle(num_rows)

##count vowels

def count_vowels(input_string):

    vowels = "aeiouAEIOU"

    
    vowel_counts = {vowel: 0 for vowel in vowels}

   
    for char in input_string:
        if char in vowels:
            vowel_counts[char] += 1

    return vowel_counts

###

def complex_addition(a_real, a_imag, b_real, b_imag):
    real_sum = a_real + b_real
    imag_sum = a_imag + b_imag
    return real_sum, imag_sum

def complex_subtraction(a_real, a_imag, b_real, b_imag):
    real_diff = a_real - b_real
    imag_diff = a_imag - b_imag
    return real_diff, imag_diff

def complex_multiplication(a_real, a_imag, b_real, b_imag):
    real_product = (a_real * b_real) - (a_imag * b_imag)
    imag_product = (a_real * b_imag) + (a_imag * b_real)
    return real_product, imag_product

def complex_division(a_real, a_imag, b_real, b_imag):
    divisor_conjugate_real = b_real
    divisor_conjugate_imag = -b_imag

    numerator_real, numerator_imag = complex_multiplication(a_real, a_imag, divisor_conjugate_real, divisor_conjugate_imag)
    denominator = (b_real ** 2) + (b_imag ** 2)

    real_quotient = numerator_real / denominator
    imag_quotient = numerator_imag / denominator

    return real_quotient, imag_quotient

# Example usage
a_real, a_imag = 3, 2
b_real, b_imag = 1, -1

# Addition
result_addition = complex_addition(a_real, a_imag, b_real, b_imag)
print("Addition:", result_addition)

# Subtraction
result_subtraction = complex_subtraction(a_real, a_imag, b_real, b_imag)
print("Subtraction:", result_subtraction)

# Multiplication
result_multiplication = complex_multiplication(a_real, a_imag, b_real, b_imag)
print("Multiplication:", result_multiplication)

# Division
result_division = complex_division(a_real, a_imag, b_real, b_imag)
print("Division:", result_division)

##

num1=10
num2=11
r1=num1%num2
print(r1)
r2=num1-num2
print(r2)
r3=num1*num2
print(r3)

###
def modify_string(input_str):
    if input_str.endswith('python'):
        return input_str + 'java'
    elif len(input_str) < 5:
        return input_str + 'php'
    else:
        return input_str + 'python'

result1 = modify_string('hello')
print(result1)  

result2 = modify_string('worldpython')
print(result2)  

result3 = modify_string('examplepython')
print(result3)  