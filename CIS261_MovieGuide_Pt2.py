# Course CIS261 Week 6 lab 2 MovieGuide pt2
# Emma Kailani Tirado 05/13/2025

MOVIE_FILE = 'movies.txt'

def display_menu():
        print("\nThe Movie List Program\n")
    print("COMMAND MENU")
    print("list - Lists all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program\n")

def display_movies(movie_list):
    print("\nMovie Titles: ")

# append() function
def add_movie(movies):
    movie_name = input("Name: ")
    movies.append(movie_name)
    print(f"{movie_name} was added. \n")


# pop() function
def del_movie(movies):
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(movies):
            removed = movies.pop(number - 1)
            print(f"{removed} was deleted.\n")
        else:
            print("Invalid movie number.\n")
    except ValueError:
        print("Please enter a valid number.\n")
#Not a valid command please try again

# add movies to list
def main():
    movie_file = "movies.txt" #["Monty Python and the Holy Grail", "On the Waterfront", "Cat on a Hot Tin Roof"]
    movie_list = populate_list(movie_file)


    #Create the while loop for commands
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