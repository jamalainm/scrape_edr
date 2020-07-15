from bs4 import BeautifulSoup, NavigableString, Tag

all_inscriptions = []

url = 'edr_roma_sepulch.html'
with open(url,'r') as f:
    page = f.read()

soup = BeautifulSoup(page,'lxml')

for br in soup.findAll('br'):
    next_s = br.nextSibling
    if not (next_s and isinstance(next_s,NavigableString)):
        continue
    next2_s = next_s.nextSibling
    if next2_s and isinstance(next2_s,Tag) and next2_s.name == 'br':
        text = str(next_s).strip()
        if text:
            print(f"Found: {next_s}")
