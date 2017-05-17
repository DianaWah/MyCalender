#NAME: WAKHASA DIANA MARTHA
#REG.NO: 15/U/1298
#CALENDER ASSIGNMENT:COMPUTER PROGRAMMING FUNDAMENTALS


import calendar

while True:
  x = input("Enter date: ")
  m = input("Enter month: ")
  y = input("Enter Year: ")
  yy = int(y)
  mm = int(m)
  xx = int(x)
  print("\n\n    My calender")
  print "====================="
  print(calendar.month(yy,mm))
  print "=====================\n\n"
