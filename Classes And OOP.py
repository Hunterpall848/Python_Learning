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

#Checks to see if the classes in the list bellow can use .count
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")


