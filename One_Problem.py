List = [-3,-2,-1,0,1,2,3,4,5]

def maximumCount(nums: List[int]) -> int:
    return max(
        len([x for x in nums if x<0]),
        len(x for x in nums if x>0)
    )