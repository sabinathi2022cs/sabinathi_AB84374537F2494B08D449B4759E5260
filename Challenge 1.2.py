def isleapyear(year):
    if (year%4==0):
      print('{}is not a leap year'.format (year))
    else:
      print('{} is not a leap year'.format (year))
year=int(input("Enter a year value"))
isleapyear(year)