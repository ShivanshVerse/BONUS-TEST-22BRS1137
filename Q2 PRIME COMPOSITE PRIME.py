"""Q2) Write a Python program using while loop to read the numbers until -1 is encountered. Count the number of prime and composite numbers entered by the user. 
Input: Numbers are given one after the other in separate lines. Give the last number as -1. 
Output: Print the count of the prime numbers using the variable name PrimeCount and the count of composite numbers using the variable name CompositeCount.
"""

def PrimeCheck(n):
  count=0
  for i in range(1,n+1,1):
    if(n%i==0):
      count+=1
  if(count==2):
    return True
  else:
    return False
PrimeCount=0
CompositeCount=0
while True:
  n=int(input())
  if n==-1:
    break
  elif PrimeCheck(n):
    PrimeCount+=1
  elif n!=1:
    CompositeCount+=1
print("primecount is",PrimeCount)
print("compositecount is",CompositeCount)