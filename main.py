
def circularArrayRotation(a, k, queries):
    # Write your code here
    
    for iter in range(k):
        curr_idx = 0
        var = a[curr_idx]
        for i in range(len(a)):
            next_idx = curr_idx + 1
            if next_idx == len(a):
                next_idx = 0
            elif curr_idx == len(a):
                curr_idx = 0
            temp = a[next_idx]
            a[next_idx] = var
            var = temp
            curr_idx += 1
    for i in queries:
        print(a[i])


circularArrayRotation([1, 2, 3, 4], 2, [1, 2])