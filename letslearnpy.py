import math

def reverse_string(s):
    """
    Function to reverse a given string.
    
    Args:
        s (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    return s[::-1]

def find_unique_elements(arr):
    """
    Function to find unique elements in a given array.
    
    Args:
        arr (list): The array to find unique elements from.
    
    Returns:
        list: A list of unique elements.
    """
    return list(set(arr))

def find_square_root(num):
    """
    Function to calculate the square root of a number.

    Args:
        num (float): The number to find the square root of.

    Returns:
        float: The square root of the number.

    Example:
        >>> find_square_root(16)
        4.0
        >>> find_square_root(25)
        5.0
    """
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(num)

def add_numbers(a, b):
    """
    Function to calculate the addition of two numbers.

    This function takes two numerical inputs, either integers or floats, 
    and returns their sum. It is designed to handle both positive and 
    negative numbers, as well as zero. The result will be in the same 
    numerical type as the inputs.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.

    Example:
        >>> add_numbers(10, 20)
        30
        >>> add_numbers(-5, 15)
        10
    """
    return a + b

# Example usage
if __name__ == "__main__":
    input_string = "hello"
    print("Original String:", input_string)
    print("Reversed String:", reverse_string(input_string))
    
    input_array = [1, 2, 2, 3, 4, 4, 5]
    print("Original Array:", input_array)
    print("Unique Elements:", find_unique_elements(input_array))

    num1 = 10
    num2 = 20
    print("Number 1:", num1)
    print("Number 2:", num2)
    print("Sum:", add_numbers(num1, num2))

    number = 16
    print("Number:", number)
    print("Square Root:", find_square_root(number))