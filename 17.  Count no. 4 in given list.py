"""
P.iotic

Q: 22. Write a Python program to count the number 4 in a given list.

Understood it when the program ran, could relate that list_count_4 can be summoned
like that.
tricky part that is holding me on halt is return, haven't fully understood it yet
"""
def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))
