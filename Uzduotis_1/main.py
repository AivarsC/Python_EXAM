# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "filter_all_or_nothing_people" - kaip argumentą priims "users"
# sąrašą ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie arba neturi
# naminių gyvūnų visiškai, arba turi ir šunį, ir katę.

# 2. funkcija "filter_underaged_owners" - kaip argumentą priims "users" sąrašą
# ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie dar nėra pilnamečiai,
# bet jau turi bent vieną naminį gyvūną.

users = [
    { 'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True },
    { 'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': False },
    { 'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True },
    { 'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': False },
    { 'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False },
    { 'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': False, 'hasCat': True },
    { 'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': False },
    { 'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': True },
    { 'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False },
]

# =================  Sprendimas  ==================

import pprint 

# 1 funkcija

def filter_all_or_nothing_people(people):
    """Grąžina vartotojus, kurie arba neturi naminių gyvūnų visiškai, arba turi ir šunį, ir katę."""

    res = []
    for person in people:
        if person['hasDog'] == False and person['hasCat'] == False or person['hasDog'] == True and person['hasCat'] == True:
            res.append(person)

    return res

# 2 funkcija

def filter_underaged_owners(owners):
    """Grąžina vartotojus, kurie dar nėra pilnamečiai, bet jau turi bent vieną naminį gyvūną."""

    res = []
    for owner in owners:
        if owner['age'] <= 18 and (owner['hasDog'] == True or owner['hasCat'] == True):
            res.append(owner)

    return res

# ===================================
# Testing:
# ===================================

pp = pprint.PrettyPrinter(indent=5)

print("# ------------Test 1 funkcija:------------")
all_or_nothing_people = filter_all_or_nothing_people(users)
pp.pprint(all_or_nothing_people)

print("# ------------Test 2 funkcija:------------")
teens = filter_underaged_owners(users)
pp.pprint(teens)

