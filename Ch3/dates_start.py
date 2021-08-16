#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class

  today=date.today()
  print(today)

  # print out the date's individual components
  print("Date components:" ,today.day,today.month,today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today weel day  is",today.weekday())
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  days =["sun","mon","tues","wed","fri","sat",]
  print ("which is a:",days[today.weekday()])
  
  # Get the current time
  today=datetime.now()
  print(today)
  time=today.time
  t= datetime.time(datetime.now())
  print(t)

  
if __name__ == "__main__":
  main();
  