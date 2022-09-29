# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.


# =================  Sprendimas  ==================

class Movie:
    """Describes movie with properties: title, director and budget"""
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def __str__(self):
        """ Returns info about movie"""
        return (f'Movie title: "{self.title}", Director: {self.director}, Budget: {self.budget} USD')

    def was_expensive(self):
        """" Return TRUE when budget is greater than 100M USD, and FAlSE when less than 100M """
        if self.budget > 100000000:
            return True
        else:
            return False

movie_1 = Movie('Pirates of the Caribbean: On Stranger Tides', 'Rob Marshall', 422000000)
movie_2 = Movie('Redirected', 'Emilis Velyvis', 2700000)

# ===================================
# Testing:
# ===================================

print(movie_1)
print('Was the movie expensive? ', movie_1.was_expensive())

print(movie_2)
print('Was the movie expensive? ', movie_2.was_expensive())
