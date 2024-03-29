# Day 5

# Try to approximate the behaviour of the is operator using ==.
books1 = ["The Godfather", "Casino Royale", "The Shining"]
movies1 = books1 # This will make both print statements contain the same memory address and be equaled to True

print(id(books1))
print(id(movies1))

print(books1 == movies1)
print(books1 is movies1)

# Now let's see what happens when movies has a list of its own
books2 = ["The Godfather", "Casino Royale", "The Shining"]
movies2 = ["The Godfather", "Casino Royale", "The Shining"]

print(id(books2))
print(id(movies2))

print(books2 == movies2)
print(books2 is movies2)
# books2 is movies2 is False, because it has a different variable name

"""
Try to use the 'is' operator or the 'id' function to investigate the difference between this:

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

And this:

numbers = [1, 2, 3, 4]
numbers.append(5)
"""

movies = ["Goldfinger", "Harry Potter and the Goblet of Fire", "Kid Galahad"]
new_movies = movies + ["2001: A Space Odyssey"]
print(id(movies))
print(id(new_movies))

print(movies == new_movies)
print(movies is new_movies)

tv = ["Father Knows Best", "Dragnet", "Dexter"]
tv.append("Star Trek")

print(id(tv))
