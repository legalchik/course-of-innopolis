

def pro(nums: list) -> int:
    res = 1
    for el in nums:
        res *= el
    return res

print(pro([1,2,3,4,5,6,7,8,9]))
