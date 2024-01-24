# Program 1: Calculate the Sum of Numbers from 1 to 5 using a while loop

sum_numbers = 0
current_number = 1

while current_number <= 5:
    sum_numbers += current_number
    current_number += 1

print("Sum:", sum_numbers)

# Program 2: Reverse a String using a while loop

original_string = "Hello"
reversed_string = ""

index = len(original_string) - 1
while index >= 0:
    reversed_string += original_string[index]
    index -= 1

print("Original:", original_string)
print("Reversed:", reversed_string)
