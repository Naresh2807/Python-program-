def max_min(arr):
    if len(arr) == 0:
        return None,None
    max_value=arr[0]
    print("max_value",max_value)
    min_value=arr[0]
    print("min_value",min_value)

    for num in arr:
        print(num,max_value)
        if num > max_value:
            print(num,max_value)
            max_value = num
        if num < min_value:
            print(num,min_value)
            min_value = num

    return max_value,min_value

array=[3, 5, 7, 2, 8]
max_value, min_value=max_min(array)

print(f"Maximum value:{max_value}")
print(f"Minimum value:{min_value}")
