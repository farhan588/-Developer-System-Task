def find_peak_element(arr):
    n = len(arr)
    if n == 0:
        return None
    if n == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[-1] > arr[-2]:
        return arr[-1]

    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return arr[i]
    return None
