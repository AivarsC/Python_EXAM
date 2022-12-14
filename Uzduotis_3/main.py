# Duotas "audi" žodynas.

# Parašykite funkciją "get_dict_values", kuri:
# * Turės 'docstring' tipo komentarą apie tai, ką ji atlieka.
# * Nekeis žodyno, priimto kaip argumento, savo viduje.
# * Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values).

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

# =================  Sprendimas  ==================

def get_dict_values(items):
  """Grąžins sąrašą su visomis jo reikšmėmis (values)."""

  return list(items.values())

# ===================================
# Testing:
# ===================================

print(get_dict_values(audi))