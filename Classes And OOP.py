import operator


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

class Math:
    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.mult = num1 * num2
        self.div = num1 / num2
        self.sub = num1 / num2
        self.add = num1 + num2



numbers1 = Math(12, 34)
print(numbers1.mult + numbers1.add - numbers1.div)


class Student:


    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []


    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)

class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))

