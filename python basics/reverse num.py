5

n=int(input())
rev=0
while n>0:
  digit=n%10
  rev=rev*10+digit
  n=n//10
print("reverse of number",rev)