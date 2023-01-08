"""Q4)Write a program that takes your full name as input and displays the abbreviations of
the first and middle names except the last name which is displayed as it is. For example, if your name is Robert Brett Roser, then the output should be R.B.Roser  
"""
n=input()
ss=n.split()
length=len(ss)
l=[]
for i in range(1,length):
  k=ss[i-1]
  l.append(k[0])
  l.append(".")
l.append(ss[length-1])
for i in l:
  print(i,end="")