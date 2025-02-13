#First Class practice showing favorite things!
class Favorites:
    def __init__(self, color, movie, song, animal):
        self.color = color
        self.movie = movie
        self.song = song
        self.animal = animal
        self.all = [color, movie, song, animal]

hunter_fav = Favorites('Red', 'Harry Potter', 'XO Tour Lif3', 'Moya')
Mckenzie_fav = Favorites('Yellow', 'Hunger Games', 'Any SZA or Adelle',
                         'Moya' )

print(hunter_fav.all)
print(Mckenzie_fav.all)


