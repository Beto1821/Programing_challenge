# Programming Challenge - Support Engineer
The purpose of this repository is to upload my Programming  Challenge for a Support Engineer position at Lexart labs.

## Intro
The objective of this challenge was to create an algorithm that traverses an array that contains string of letters and numbers.
#### The results must have:
+ An array containing only letters;
+ An array containing only numbers;
+ Obtain the largest number from the numbers array.

## Methodology
To perform this challenge I chose Python as the main programming language.

Developing the solution I choose to create two functions to resolve this problem;
```python
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
```

## Results Analysis
 ```exemple_array = ["a", 10, "b", "hello", 122, 15]```, as an argument for ```array_through(exemple_array)``` function, unpacking the return in two variables, ```letters``` and ```numbers```. Then with two prints, we can see the results obtained:
+ ```Only letters array: ['a', 'b', 'hello']```
+ ```Only numbers array: [10, 122, 15]```
  
To analize the ```find_largest_number(array)```, I called it with the ```numbers``` variable unpacked as an argument, and stored at a new variable, ```find_largest_number```. The final result is showed at the last print:
+ ```Largest number: 122```

The algorithm created was able to iterate through all array inputted, obtaining:
+ An array containing only letters;
+ An array containing only numbers;
+ A variable with the largest number.