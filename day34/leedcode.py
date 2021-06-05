# nums = [3,1,2,4]
# mmm= []
# nnn=[]
# for i in nums:
#     if i % 2==0:
#         mmm.append(i)
# mmm.extend(nnn)        
# print(mmm)


# class Solution:
#     def sortArrayByParity(self):


    # def sortArrayByParity(self, nums: List[int]) -> List[int]:



grid = [
    [4,3,2,-1],
    [3,2,1,-1],
    [1,1,-1,-2],
    [-1,-1,-2,-3]
]

t = 0

for item in set(grid):
    if grid.count(item) == 0:
        t +=item
print(t)
    
     #nums = [1,2,3,2,1,2,3,4,5,6,7,8,9,10]
# unikalnayaSumma = 0 
# for i in set(nums): 
#     if nums.count(i) == 1:
#         unikalnayaSumma += i
# print(unikalnayaSumma)