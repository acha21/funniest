from markdown import markdown

def joke():
    return markdown(u'Wenn ist das Nunst\u00fcck git und Slotermeyer?'
                    u'Ja! ... **Beiherhund** das Oder die Flipperwaldt '
                    u'gersput.')
    

def print_raw():
    import os
    
    cur = os.path.dirname(os.path.abspath(__file__))
    print(cur)
    with open(os.path.join(cur, "data/raw.txt"), "r") as rf:
        for line in rf:
            print(line)