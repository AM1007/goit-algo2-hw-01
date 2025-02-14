def quick_select(arr, k):
    """
    Finds the k-th smallest element in an unsorted array
    using the Quick Select algorithm.
    
    Args:
        arr: list of numbers
        k: the order of the desired element (starting from 1)
    
    Returns:
        The k-th smallest element of the array
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the length of the array")
    
    # Convert k to an index (k-1, since array indexing starts at 0)
    return quick_select_helper(arr, 0, len(arr) - 1, k - 1)

def quick_select_helper(arr, left, right, k):
    # Base case: if the segment contains one element
    if left == right:
        return arr[left]
    
    # Partition the array around a pivot element
    pivot_idx = partition(arr, left, right)
    
    if k == pivot_idx:
        # Found the desired element
        return arr[k]
    elif k < pivot_idx:
        # The desired element is in the left part
        return quick_select_helper(arr, left, pivot_idx - 1, k)
    else:
        # The desired element is in the right part
        return quick_select_helper(arr, pivot_idx + 1, right, k)

def partition(arr, left, right):
    """
    Partitions the array around a pivot element.
    All elements smaller than the pivot are moved to the left, larger ones to the right.
    """
    # Choose the pivot element (in this case, the last element)
    pivot = arr[right]
    
    # Index for elements smaller than the pivot
    i = left
    
    # Move elements smaller than the pivot to the left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    # Place the pivot element in its correct position
    arr[i], arr[right] = arr[right], arr[i]
    return i

# Testing the function
def test_quick_select():
    # Test 1: regular case
    arr1 = [7, 4, 6, 3, 9, 1]
    assert quick_select(arr1.copy(), 2) == 3  # 2nd smallest element
    assert quick_select(arr1.copy(), 1) == 1  # 1st smallest element
    assert quick_select(arr1.copy(), 6) == 9  # largest element
    
    # Test 2: array with duplicate elements
    arr2 = [5, 2, 5, 2, 5, 2]
    assert quick_select(arr2.copy(), 2) == 2
    assert quick_select(arr2.copy(), 4) == 5
    
    # Test 3: array with a single element
    arr3 = [42]
    assert quick_select(arr3, 1) == 42
    
    # Test 4: array with negative numbers
    arr4 = [-3, 5, -8, 12, 0, -1]
    assert quick_select(arr4.copy(), 1) == -8  # smallest element
    assert quick_select(arr4.copy(), 3) == -1  # 3rd smallest element
    
    try:
        quick_select(arr1, 7)  # k greater than array length
        assert False, "An exception should have been raised"
    except ValueError:
        pass
    
    print("All tests passed successfully!")

# Run tests
test_quick_select()
