# leap year program
def isleapyear(year):
  if(year%4==0):
    print("{} year is leap year ".format(year))
  else:
    print("{} year is not leap year".format(year))
year=int(input("Enter a year value"))
isleapyear(year)
  
