def max_subarray_sum(arr):
    if not arr:
        raise ValueError("The input array is empty")
            current_max = global_max = arr[0]
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        global_max = max(global_max, current_max)
    return global_max
