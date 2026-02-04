def swap_case(s):
    arr = list(s)
    for i in range(len(arr)):
        if arr[i].isalpha():
            arr[i] = arr[i].lower() if arr[i].isupper() else arr[i].upper()
    return "".join(arr)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)