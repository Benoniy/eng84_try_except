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
    try:  # Try and open it
        file = open(filename)
        print("File opened")
    except FileNotFoundError as errormsg:  # if it doesnt exist
        file = open(filename, "w")
        print("File opened")
        file.write("empty right now")
        file.close()
        file = open(filename, "r")
    finally:
        print("\n" + file.name, "list: ")
        for f in file.readlines():
            print(f, end="")


def open_and_addto_file(filename, write):
    try:  # Try and open it
        file = open(filename, "a")
        print("File opened")
    except FileNotFoundError as errormsg:  # if it doesnt exist
        print("Unknown error: ", errormsg)
    finally:
        file.write("\n"+write)
        file.close()


if __name__ == "__main__":
    open_and_list_file("orders.txt")
    open_and_addto_file("orders.txt", "ball")

