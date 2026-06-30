def bubble_sort(arr: list) -> None:
    """Sort the array using bubble sort (in-place).

    Args:
        arr: list to be sorted (modified in-place)
    """
    n = len(arr)
    for i in range(n-1):
        check_flag = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                check_flag = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if not check_flag:
            break
        


def insertion_sort(arr: list) -> None:
    """Sort the array using insertion sort (in-place).
    Args:
        arr: list to be sorted (modified in-place)
    """
    length = len(arr)
    for i in range(1,length):
        target = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = target
    

    


def merge_sort(arr: list) -> list:
    """Sort the array using merge sort (out-of-place).

    Args:
        arr: list to be sorted (not modified)

    Returns:
        New sorted list
    """
    # Replace the code below with your implementation
    raise NotImplementedError


def quick_sort(arr: list) -> list:
    """Sort the array using quick sort (out-of-place).

    Args:
        arr: list to be sorted (not modified)

    Returns:
        New sorted list
    """
    # Replace the code below with your implementation
    raise NotImplementedError
