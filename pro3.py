def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [int(line.strip()) for line in lines]

file_path = '1'
arr = read_file(file_path)

def divide(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    lh, _ = divide(arr[:mid])
    rrh, __ = divide(arr[mid:])
    new_arr, ans = merge_count(lh,rrh)

    return new_arr, _ + __ + ans

def merge_count(lh,rrh):
    i=j=ans=0
    new_arr=[]

    while i < len(lh) and j < len(rrh):
        if lh[i] <= rrh[j]:
            new_arr.append(lh[i])
            i += 1
        else:
            new_arr.append(rrh[j])
            j += 1
            ans += (len(lh)-i) # [3,2/1]

    new_arr += lh[i:]
    new_arr += rrh[j:]

    return new_arr , ans


new_arr, ans = divide(list(arr))
print(ans)
