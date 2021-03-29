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

# File creation and modification