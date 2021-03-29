# Exception handling


# Try to open a file that doesnt exist
try:
    file = open("ordas.txt")
    print("File opened")
except FileNotFoundError as errormsg:
    print("File not found, ERROR:", errormsg)
finally:

    print("Oh well at least finally is working!")


# Try to open a file that does exist
try:
    file = open("orders.txt")
    print("File opened")
except FileNotFoundError as errormsg:
    print("File not found, ERROR:", errormsg)
finally:
    print("Oh well at least finally is working!")


# Task - read the data from a file and print it


# Open a file and list the contents
def open_and_list_file(filename):
    try:
        file = open(filename)
        print("File opened")
    except FileNotFoundError as errormsg:
        print("File not found, ERROR:", errormsg)
    finally:
        print("\n" + file.name, "list: ")
        for f in file.readlines():
            print(f, end="")


open_and_list_file("movies.txt")

