import urllib
from bs4 import BeautifulSoup
#from BeautifulSoup import *

i = 0
links = list()
links.append("http://www.du.ac.in/du/index.php?page=amenities")
#url = "http://www.du.ac.in/du/index.php?page=amenities"
fhand = open("linksfile.txt","w")
pdfHand = open("pdfFile.txt","w")
for link in links:
  print(len(links),i,link)
  i+=1
  try:
    #print link
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html5lib")
    tags = soup('a')
    for tag in tags:
      try:
        linknew = tag.get('href', None)
        linknew.encode('utf-8')
#        print(linknew)
        if linknew == "http://www.du.ac.in/du":
          continue
        if '#' in linknew or "mact" in linknew or linknew in links:
          continue
        if not linknew.startswith("http://www.du.ac.in"):
          continue
        if 'jpg' in linknew or 'png' in linknew or 'upload' in linknew:
          continue
        if 'pdf' in linknew:
          pdfHand.write(linknew)
          pdfHand.write("\n")
          continue
        links.append(linknew)
        fhand.write(linknew)
        fhand.write("\n")
      except:
        continue
  except:
    continue

for link in links:
  print(link)

