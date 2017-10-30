import urllib
from bs4 import BeautifulSoup
#from BeautifulSoup import *
import sys

def checklinkvalidity(linknew):
  validity = 1
  if linknew == "http://www.du.ac.in/du/":
          validity = 0
  if '#' in linknew or "mact" in linknew or linknew in links:
          validity = 0
  if not linknew.startswith("http://www.du.ac.in"):
          validity = 0  
  if 'jpg' in linknew or 'png' in linknew or 'upload' in linknew:
          validity = 0
  return validity

i = 0
links = list()
links.append("http://www.du.ac.in/du/index.php?page=amenities")
#url = "http://www.du.ac.in/du/index.php?page=amenities"
fhand = open("linksfile.txt","w")
pdfHand = open("pdfFile.txt","w")
html = urllib.request.urlopen(links[0]).read()
soup = BeautifulSoup(html,"html5lib")

divtag = soup.find('div', attrs={"class" : "grid_3 pull_9"})
tags = divtag.find_all('a')

for href in tags:
  print(href['href'])
  print(checklinkvalidity(href['href']))
  if checklinkvalidity(href['href']):
    links.append(href['href'])
    #print href['href']
    fhand.write(href['href'])
    fhand.write("\n")

print(links)
for link in links:
  print(len(links),i,link)
  i+=1
  try:
    #print link
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html,"html5lib")
    divtag = soup.find('div', attrs={"class" : "content-inner grid_9 push_3"})
    tags = divtag.find_all('a')
    print(tags)
    for tag in tags:
      try:
        linknew = tag[href]
#        print(linknew)
        if checklinkvaladity(linknew) == 1:
          print(linknew)
          if 'pdf' in linknew:
            pdfHand.write(linknew)
            pdfHand.write("\n")
            continue
          links.append(linknew)
          fhand.write(linknew)
          fhand.write("\n")
        else:
          continue
      except:
        continue
  except:
    continue

for link in links:
  print(link)

