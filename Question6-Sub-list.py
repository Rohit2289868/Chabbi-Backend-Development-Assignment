def f(arr, start, end, ans):
    for i in range(start, end, 2):
        ans.append(arr[i])
        

ans = []
f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9, ans)
print(ans)