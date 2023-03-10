count = [-12,-10,-9,-7,-5,-3,-2,-1,0,1,2,3,4,5,8,9,12,18]

def maximumCount(nums):
    return list[max(
        len([x for x in nums if x<0]),
        len([x for x in nums if x>0])
    ),
    min(
        len([x for x in nums if x<0]),
        len([x for x in nums if x>0])
    )]

print(maximumCount(count))

