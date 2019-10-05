#!/usr/bin/env python3
# namelookup.py - Program to display name statistics
# James Skon, 2019
#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()
fileName="/home/class/SoftDev/marvel/marvel-wikia-data.csv"

class CharacterEntry: 
  def __init__(self, line : str):
    line=line.strip()
    data=line.split(",")
    self.pageid=data[0]
    self.char=data[1]
    self.urlslug=data[2]
    self.identify=data[3]
    self.alignment=data[4]
    self.eyecolor=data[5]
    self.hair=data[6]
    self.sex=data[7]
    self.gsm=data[8]
    self.alive=data[9]
    self.appearances=data[10]
    self.first_appear=data[11]
    self.year=data[12]

 
class TheIndex: 
  def __init__(self, fileName : str): 
    char_names = open(fileName)
    self.charmap={}
    self.chars=[]
    index=0
    for line in char_names:  
      charData=CharacterEntry(line) 
      self.chars.append(charData) 
      fullname=charData.char 
      names=fullname.lower().split(" ") 
      for name in names: 
        if name in self.charmap:
            self.charmap[name].append(index)
        else: 
            self.charmap[name]=[index] 
      index+=1  
    return
  def getResults(self,user_entry): 
    return self.charmap.get(user_entry) 


def print_header():
    print ("""Content-type: text/html\n""")


def main(): 
  form = cgi.FieldStorage()
  if (form.getvalue("name") and form.getvalue("type_select")):
    print_header()
    name=form.getvalue("name").upper()
    ltype=form.getvalue("type_select")
    if ltype=="charName":
        full_charmap=TheIndex(fileName) 
        user_entry="peter"
        print("Looking up matches for the name","'"+user_entry+"'"+". . .")
        l=full_charmap.getResults(user_entry) 
        print(l)
     else:
        print("idk")
  else:
      print("Error in submission")
main()