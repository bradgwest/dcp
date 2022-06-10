def reconstruct(arr):
    result = []
    n = len(arr) - 1
    stack = []

    for i in range(n):
        if arr[i + 1] == "-":
            stack.append(i)
        else:
            print(f"i={i}, arr_plus_1={arr[i+1]}; stack={stack}")
            result.append(i)
            while stack:
                result.append(stack.pop())

    stack.append(n)

    while stack:
        result.append(stack.pop())

    return result


# print(reconstruct([None, "+", "+", "-", "+"]))
print(reconstruct([None, "-", "-", "+", "+"]))
