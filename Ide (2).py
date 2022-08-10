#leap year or not.....
def getly(year):
  if year % 4==0:
    if year % 100==0:
      if year % 400==0:
        print("Yes")
      else:
        print("No")
    else:
      print("Yes")
  else:
    print("No")
for _ in  range(int(input())):
  getly(int(input()))
  
