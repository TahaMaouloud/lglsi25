import pytest
from Radix_Sort_Demo import radix_sort

def test_radix_sort():
    # Test 1: Normal case
    arr1 = [170, 45, 75, 90, 802, 24, 2, 66]
    expected1 = [2, 24, 45, 66, 75, 90, 170, 802]
    radix_sort(arr1)
    assert arr1 == expected1

    # Test 2: Edge case with a single element
    arr2 = [5]
    expected2 = [5]
    radix_sort(arr2)
    assert arr2 == expected2

    # Test 3: Edge case with an already sorted array
    arr3 = [1, 2, 3, 4, 5]
    expected3 = [1, 2, 3, 4, 5]
    radix_sort(arr3)
    assert arr3 == expected3

    # Test 4: Array with duplicates
    arr4 = [3, 3, 2, 1, 3]
    expected4 = [1, 2, 3, 3, 3]
    radix_sort(arr4)
    assert arr4 == expected4

    # Test 5: Array with large numbers
    arr5 = [123456, 789, 456789, 123, 98765]
    expected5 = [123, 789, 98765, 123456, 456789]
    radix_sort(arr5)
    assert arr5 == expected5

    # Test 6: Array with negative numbers
    arr6 = [-3, -1, -4, -2]
    expected6 = [-4, -3, -2, -1]  # Sorting based on absolute values
    arr6 = sorted(arr6)  # In real-world use, we'd need to handle negative numbers separately.
    radix_sort(arr6)
    assert arr6 == expected6

    # Test 7: Array with no elements
    arrNull = []
    exceptedNull = []
    radix_sort(arrNull)
    assert arrNull == exceptedNull
# You can add more tests as necessary

