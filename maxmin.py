def find_min_max(arr):
    # Initialize min and max with the first element of the array
    min_element = arr[0]
    max_element = arr[0]

    # Iterate through the array to find the min and max
    for element in arr:
        if element < min_element:
            min_element = element
        if element > max_element:
            max_element = element

    return min_element, max_element

# Example usage
array = [3, 1, 4, 6, 2, 7]
min_element, max_element = find_min_max(array)
print(f"Minimum element: {min_element}")
print(f"Maximum element: {max_element}")
print(f"Output: {min_element}, {max_element}")
