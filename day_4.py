movies = [("2001: A Space Odyssey", "Stanley Kubrick", 1968, 10500000)]
title = input("What is the title of the movie? ")
director = input("Who is the director? ")
year = int(input("What year was the movie released? "))
budget = int(input("What was the movie's budget? "))

new_movie = (title, director, year, budget)
print(f"{new_movie[0]} was released in {new_movie[2]}")

movies.append(new_movie)

movies.pop(0)

print(movies)
