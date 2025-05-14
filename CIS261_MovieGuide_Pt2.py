# Course CIS261 Week 6 lab 2 MovieGuide pt2
# Emma Kailani Tirado 05/13/2025

# call/write in file movies.txt

def movie_guide():
        print("\nThe Movie List Program\n")
    print("COMMAND MENU")
    print("list - Lists all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program\n")

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





if __name__ == "__main__":
    main()