# Course CIS261 Week 6 lab 2 MovieGuide pt2
# Emma Kailani Tirado 05/13/2025

# Create a new file named 'movie.txt' and write the 3 movies into it
FILENAME = 'movies.txt'

# write
def write_movies(movies): 
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(f"{movie}\n")

# Read
def read_movies():
    try:
        with open(FILENAME, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return none

#list
def list_movies(movies):
    print("\nThe Movie List")
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}\n")

# add /append() function
def add_movie(movies):
    movie_name = input("Name: ")
    movies.append(movie_name)
    write_movies(movies)
    print(f"{movie_name} was added. \n")

# delete /pop() function
def del_movie(movies):
    try:
        index = int(input("Number: "))
        if index < 1 or index > len(movies):
            print("Invalid movie number.\n")
        else:
            movie = movies.pop(index -1)
            write_movies(movies)
            print(f"\n{movie} was deleted. \n")
    except FileNotFoundError:
        return none

def display_menu():
    print("\nThe Movie List Program\n")
    print("COMMAND MENU")
    print("list - Lists all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program\n")

def main():
    movies = read_movies()
    if movies is None:
        print("\nFile not found. Starting with an empty list." )
        movies = []

    display_menu()


    while True:
        command = input("Command: ").lower()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            del_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()