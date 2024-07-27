def sum_even_odd_indexed_elements(arr):
    even_sum = 0
    odd_sum = 0

    for index, element in enumerate(arr):
        if index % 2 == 0:
            even_sum += element
        else:
            odd_sum += element

    return even_sum, odd_sum

# Example usage
array = [1, 2, 3, 4, 5, 6, 7]
even_sum, odd_sum = sum_even_odd_indexed_elements(array)
print(f"Sum of elements at even indices: {even_sum}")
print(f"Sum of elements at odd indices: {odd_sum}")
print(f"Output array: {even_sum} {odd_sum}")
