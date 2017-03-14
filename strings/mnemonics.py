__author__ = 'nrao'

def two():
    options = ['A', 'B', 'C']
    for option in options:
        yield option

def three():
    options = ['D', 'E', 'F']
    for option in options:
        yield option

def mnemonics():
    t = two()
    for val in t:
        th = three()
        for item in th:
            yield val + item

for mne in mnemonics():
    print mne
