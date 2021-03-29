# Exception Handling
### Keywords:
* `try:` - Attempt to run this code.


* `except ErrorType:` - Execute if ErrorType is thrown.  


* `finally:` - Executes after the try and except no matter the outcome.  


* `raise ErrorType("message")` - manually raises an error.


### Example: 
```python
# Try to open a file that does exist
try:
    file = open("orders.txt"  # Try and open a file
    print("File opened")
except FileNotFoundError as errormsg:  # if it fails
    print("File not found, ERROR:", errormsg)
finally:  # Despite anything before
    print("Oh well at least finally is working!")
```  

# File creation and modification:
### Keywords:  
* `open(filename, mode)` - How to open a file
  

* List file open modes:  

| Mode |Description|  
|:---- |:----  
|'r' |This is the default mode. It Opens file for reading. |  
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|  
|'x' |Creates a new file. If file already exists, the operation fails.|  
|'a' |Open file in append mode. If file does not exist, it creates a new file.|  
|'t' |This is the default mode. It opens in text mode.|  
|'b' |This opens in binary mode.|  
|'+' |This will open a file for reading and writing (updating)|  

### Task 1 - read the data from a file and print it:  
```python
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
```

### Task 2 - Write an additional line of information to orders.txt:  
```python
def open_and_addto_file(filename, write):
    try:  # Try and open it
        file = open(filename, "a")
        print("File opened")
    except FileNotFoundError as errormsg:  # if it doesnt exist
        print("Unknown error: ", errormsg)
    finally:
        file.write("\n" + write)
        file.close()
```