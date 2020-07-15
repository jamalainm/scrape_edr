from bs4 import BeautifulSoup, NavigableString, Tag
import json

def write_corpus(corpus):
    with open('insc_sep.json','w') as f:
        json.dump(corpus,f)

def unescape(in_str):
    """Unicode-unescape string with only some characters escaped. """
    in_str = in_str.encode('unicode-escape')   # bytes with all chars escaped (the original escapes have the backslash escaped)
    in_str = in_str.replace(b'\\\\u', b'\\u')  # unescape the \
    in_str = in_str.decode('unicode-escape')   # unescape unicode
    return in_str

def alt_paragraph_contents():
    """ can I use 'contents' on 'p' tags? """

    url = 'edr_roma_sepulch.html'
    with open(url,'r') as f:
        page = f.read()

    soup = BeautifulSoup(page,'lxml')

    paragraphs = soup.findAll('p')

    no_of_paragraphs = len(paragraphs)

    corpus = []

    for i,p in enumerate(paragraphs):
        inscription = []
        for e in p.contents:
            if isinstance(e,Tag):
                for i in e.contents:
                    if isinstance(i,NavigableString):
                        i = i.string.strip().replace("\n","")
                        i = i.replace('\u00a0',' ')
                        i = i.replace('\u00ab','«')
                        i = i.replace('\u00bb','»')
                        if len(i) > 0:
                            if '<!' not in i:
                                inscription.append(i)
            if isinstance(e,NavigableString):
                e = e.string.strip().replace("\n","")
                e = e.replace('\u00a0',' ')
                e = e.replace('\u00ab','«')
                e = e.replace('\u00bb','»')
                if len(e) > 0:
                    inscription.append(e)

        corpus.append(inscription)

    return corpus


def paragraph_contents():
    """ trying to get the source and genre info, too """

    url = 'edr_roma_sepulch.html'
    with open(url,'r') as f:
        page = f.read()

    soup = BeautifulSoup(page,'lxml')

    all_entries = []

    for p in soup.findAll('p'):
        entry = []
        for e in p:
            if isinstance(e, NavigableString):
                e = e.replace('\xa0','')
                e = e.replace('\xc2','')
                e = e.replace('\n','')
                if len(e) > 0:
                    entry.append(e)

        if len(entry) > 0:
            all_entries.append(entry)

    for entry in all_entries:
        print(entry)

def just_text():
    """ This only retrieves the text of the inscriptions """
    url = 'edr_roma_sepulch.html'
    with open(url,'r') as f:
        page = f.read()

    soup = BeautifulSoup(page,'lxml')

    entries = []

    for br in soup.findAll('br'):
        entry = {}
        next_s = br.nextSibling
        if not (next_s and isinstance(next_s,NavigableString)):
            continue
        next2_s = next_s.nextSibling
        if next2_s and isinstance(next2_s,Tag) and next2_s.name == 'br':
            text = str(next_s).strip()
            if text:
                entry['text'] = next_s

        entries.append(entry)

    for entry in entries:
        print(entry)

if __name__ == '__main__':
    corpus = alt_paragraph_contents()
    write_corpus(corpus)
