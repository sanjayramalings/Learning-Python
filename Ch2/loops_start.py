#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  #while (x<5):
   # print(x)
   # x=x+1

  # define a for loop
  for x in range(5, 10):
    print(x)
    #iteartors (over a range of numbers)

  # use a for loop over a collection
  m=7
  days=["Mon","tues","e","eaaa","aaa"]
  for d in days:
    
    print(d+str(m))
    m=m+1
  
  # use the break and continue statements
  for x in range(5,10):
   #if (x==7):break
   if(x%2==0):continue
   print(x)

  #using the enumerate() function to get index 
  m=7
  days=["one","two","three","four","five"]
  for i,d in enumerate(days):  
    print(d,i)
    




if __name__ == "__main__":
  main()
