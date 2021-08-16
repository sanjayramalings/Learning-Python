# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser
metacount=0;
class MyHTMLParser(HTMLParser):
  def handle_comment(self,data):
    print("Encouneterd comment",data)
    pos =self.getpos()
    print("/tAt Line: ",pos[0],"postion",pos[1])
  def handle_starttag(self,tag,attrs):
    global metacount
    if tag =='meta':
      metacount +=1
    print ("Encounterd tag: ",tag)
    pos=self.getpos()
    print("/tAt Line: ",pos[0],"postion",pos[1])

    if attrs.__len__()>0:
      print("/Attributes: ")
      for a in attrs:
        print("\t",a[0],"=",a[1])



  def handle_endtag(self,tag):
    print("Encouneterd tag",tag)
    pos =self.getpos()
    print("/tAt Line: ",pos[0],"postion",pos[1])
    

  def handle_data(self,data):
    if (data.isspace()):
     return
    print("Encountered data :",data)
    pos=self.getpos()
    print("/tAt Line: ",pos[0],"postion",pos[1])


def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f=open("samplehtml.html")
  if f.mode =='r':
    contents =f.read()
    parser.feed(contents)
  print(str(metacount))  

if __name__ == "__main__":
  main();
  