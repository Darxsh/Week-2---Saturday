def most_frequent_element(arr):
    frequency_dict = {}
    
    # Count the frequency of each element
    for element in arr:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    
    # Find the element with the maximum frequency
    most_frequent = max(frequency_dict, key=frequency_dict.get)
    max_count = frequency_dict[most_frequent]
    
    return most_frequent, max_count

# Example usage
array = [1, 3, 2, 1, 4, 1]
element, count = most_frequent_element(array)
print(f"{element} appears {count} times in the array.")
