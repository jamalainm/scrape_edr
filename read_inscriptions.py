import json

def load_inscriptions():
    with open('insc_sep.json','r') as f:
        return json.load(f)

def write_inscriptions(texts):
    with open('inscriptions.json','w') as f:
        json.dump(texts,f)

def find_text(inscription):
    """ returns text relative to 'place' position """
    place_i = None
    if len(inscription) > 4:
        place_i = inscription.index("place:")
    if place_i:
        return inscription[place_i + 2]

def make_entry(inscription):
    """ returns a dictionary of the entries """
    entry = {}
    if 'publication:' in inscription:
        entry['publication'] = inscription[1]

        if 'province:' in inscription:
            i = inscription.index('province:')
            entry['province'] = inscription[i + 1]

        if 'place:' in inscription:
            i = inscription.index('place:')
            entry['place'] = inscription[i + 1]
            entry['text'] = inscription[i + 2]

        if 'dating:' in inscription:
            i = inscription.index('dating:')
            entry['date'] = (i + 1, i + 3)

        return entry

def make_list_of_dicts(corpus):
    """ Put together a list of dicts of inscriptions """
    texts = []
    for i in corpus:
        entry = make_entry(i)
        if entry is not None:
            texts.append(entry)

    return texts

if __name__ == '__main__':
    corpus = load_inscriptions()
    texts = make_list_of_dicts(corpus)
    write_inscriptions(texts)
