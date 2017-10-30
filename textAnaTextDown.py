import urllib
from bs4 import BeautifulSoup
import os
import sys
fhand = open('linksfile.txt', 'r')
links = fhand.read()
links = links.split('\n')
root = os.getcwd()
for link in links:
  html = urllib.request.urlopen(link).read()
  soup = BeautifulSoup(html, 'html5lib')
  
  # kill all script and style elements
  for script in soup(["script", "style"]):
    script.extract()    # rip it out
    
  divtag = soup.find_all('div', attrs={"class" : "content-inner grid_9 push_3"})
  text = ""
  for div in divtag:
    para = div.get_text().strip()
    text = text + "\n" + para

  filename = root + "/files/"+link.split('=')[1]+".txt"
  print(filename)
  f = open(filename, 'w')
  f.write(text)
