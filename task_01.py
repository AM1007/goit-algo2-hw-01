def find_min_max(arr):
    # Base case: if the array has one element
    if len(arr) == 1:
        return (arr[0], arr[0])
    
    # Base case: if the array has two elements
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))
    
    # Find the middle of the array
    mid = len(arr) // 2
    
    # Recursively find the minimum and maximum for the left and right parts
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    
    # Return the overall minimum and maximum
    return (min(left_min, right_min), max(left_max, right_max))

# Testing the function
def test_find_min_max():
    # Test 1: regular array
    arr1 = [5, 2, 9, 1, 7, 6, 3]
    assert find_min_max(arr1) == (1, 9)
    
    # Test 2: array with identical elements
    arr2 = [4, 4, 4, 4]
    assert find_min_max(arr2) == (4, 4)
    
    # Test 3: array with a single element
    arr3 = [42]
    assert find_min_max(arr3) == (42, 42)
    
    # Test 4: array with two elements
    arr4 = [10, 5]
    assert find_min_max(arr4) == (5, 10)
    
    # Test 5: array with negative numbers
    arr5 = [-3, 5, -8, 12, 0, -1]
    assert find_min_max(arr5) == (-8, 12)
    
    print("All tests passed successfully!")

# Run tests
test_find_min_max()
