import pprint

# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "get_user_average_age" - kaip argumentą priims "users" sąrašą ir
# duoto sąrašo atveju grąžins visų vartotojų amžiaus vidurkį kaip skaičių,
# suapvalintą iki artimiausio sveikojo skaičiaus.

# 2. funkcija "get_users_names" - kaip argumentą priims sąrašą ir duoto sąrašo
# atveju grąžins sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka,
# pvz. ['Alex John', 'Ann Smith', ...].

users = [
  { 'id': '1', 'name': 'John Smith', 'age': 20 },
  { 'id': '2', 'name': 'Ann Smith', 'age': 24 },
  { 'id': '3', 'name': 'Tom Jones', 'age': 31 },
  { 'id': '4', 'name': 'Rose Peterson', 'age': 17 },
  { 'id': '5', 'name': 'Alex John', 'age': 25 },
  { 'id': '6', 'name': 'Ronald Jones', 'age': 63 },
  { 'id': '7', 'name': 'Elton Smith', 'age': 16 },
  { 'id': '8', 'name': 'Simon Peterson', 'age': 30 },
  { 'id': '9', 'name': 'Daniel Cane', 'age': 51 },
]


# =================  Sprendimas  ==================

# 1 funkcija

def get_user_average_age(persons):
  """ Grąžina visų vartotojų amžiaus vidurkį kaip skaičių, suapvalintą iki artimiausio sveikojo skaičiaus """

  average = round((sum(item['age'] for item in persons))/len(persons))
  return average
 
# 2 funkcija
  
def get_users_names(people):
  """Grąžins sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka"""
  return sorted([item['name'] for item in people])


# ===================================
# Testing:
# ===================================

print("# ------------Test 1 funkcija:------------")
print('Vartotojų amžiaus vidurkis:')
print(get_user_average_age(users))


print("# ------------Test 2 funkcija:------------")
print('Vartotojų vardai abėcėlės tvarka:')
users_names = get_users_names(users)
print(users_names)
