n = int(input("Enter the number: "))

if n == 0 or n == 1:
    print(n)
else:
    start = 1
    end = n
    result = 0
    while start <= end:
        mid = (start + end) // 2

        if mid * mid == n:
            result = mid
            break
        if mid * mid < n:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    print("The floor value of the square root is:", result)
