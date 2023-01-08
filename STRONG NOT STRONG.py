"""Q3)Write a Python Code to check whether the number that is given by the user is a STRONG number or not.
Continue getting the numbers till -1 is pressed by the user. Display the count of both the cases.
Input: Get values one after the other from the user till the user enters -1.
Output: Display the count of STRONG and NOT_STRONG numbers
"""

STRONG=0
NOT_STRONG=0
fact=1
X=0
def fact(n):
  factorial=1
  for i in range(1,int(n+1)):
    factorial*=i
  return factorial
while True:
  n=int(input())
  if n==-1:
    break
  else:
    s=n
    sum=0
    while (s>0):
      d=s%10
      x=fact(d)
      sum=sum+x
      s=s/10
    if(sum==n):
      STRONG+=1
    else:
      NOT_STRONG+=1
print("STRONG_NUMBERS_COUNT is",STRONG)
print("NON_STRONG_NUMBERS_COUNT is",NOT_STRONG)