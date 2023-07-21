def separate_letters_and_numbers(arr):
    letters = [
        item for item in arr if isinstance(item, str) and item.isalpha()
        ]
    numbers = [item for item in arr if isinstance(item, int)]
    return letters, numbers


def find_largest_number(numbers):
    return max(numbers)


# Given one-dimensional array
input_array = ["a", 10, "b", "hello", 122, 15]

# Separate letters and numbers
letters_array, numbers_array = separate_letters_and_numbers(input_array)

# Find the largest number
largest_number = find_largest_number(numbers_array)

print("Array containing only letters:", letters_array)
print("Array containing only numbers:", numbers_array)
print("Largest number from the array:", largest_number)
