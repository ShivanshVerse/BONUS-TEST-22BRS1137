'''Q1) Write a Python program using while loop to read numbers until -1 is encountered. Count the numbers divisible by 4 and not divisible by 4 and display them.
Input: Get numbers using while loop until -1 is encountered separated by a space and not tab
Output: Display the count of the numbers divisible by 4 using the variable named Four_Divisible_Count and the count of the numbers not divisible by 4 using the variable named Four_Not_Divisible_Count
'''

Four_Divisible_Count=0
Four_Not_Divisible_Count=0
while True:
   n=int(input())
   if n==-1:
     break
   elif n%4==0:
      Four_Divisible_Count+=1
   else:
      Four_Not_Divisible_Count+=1
print("Four_Divisible_Count is",Four_Divisible_Count)
print("Four_Not_Divisible_Count is",Four_Not_Divisible_Count)