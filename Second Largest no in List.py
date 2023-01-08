"""Q5)Write a Python code to display the second largest number in the given list of numbers without sorting the list.
Input: Set of numbers are given in the Python data structure named list.
Output: Second largest number in that list is display.
"""

l=[]
while True:
  n=int(input())
  if n==-1:
    break
  else:
    l.append(n)
maximum=max(l)
l.remove(maximum)
maximum=max(l)
print(maximum)