try:
    a = 5
    b = 0
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Division by zero error occurred")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
