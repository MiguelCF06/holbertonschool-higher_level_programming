# Almost a Circle Python
## Objectives:bulb:
This project is a review of everything learned in Python up until 09/13/17:
* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file
* args and kwargs
* Serialization/Deserialization
* JSON

## Resources:books:
Read or watch:
* [args/kwargs](https://intranet.hbtn.io/rltoken/LroIjBBI5Gqq3ciR-OHmxg)
* [JSON encoder and decoder](https://intranet.hbtn.io/rltoken/TY4rfu2AZtXlRmPVNZm1Lw)
* [unittest module](https://intranet.hbtn.io/rltoken/T7uxwxtGdbRRW9pkD4eO0g)
* [Python test cheatsheet](https://intranet.hbtn.io/rltoken/SfEo3RQeAXXYI9yabFRw3g)

---

### [0. If it's not tested it doesn't work](./tests/)
* All your files, classes and methods must be unit tested and be PEP 8 validated. 
### [1. Base class](./models/base.py)
* Write the first class Base:
### [2. First Rectangle](./models/rectangle.py)
* Write the class Rectangle that inherits from Base:
### [3. Validate attributes](./models/rectangle.py)
* Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):
### [4. Area first](./models/rectangle.py)
* Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
### [5. Display #0](./models/rectangle.py)
* Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.
### [6. __str__](./models/rectangle.py)
* Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
### [7. Display #1](./models/rectangle.py)
* Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
### [8. Update #0](./models/rectangle.py)
* Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:
### [9. Update #1](./models/rectangle.py)
* Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:
### [10. And now, the Square!](./models/square.py)
* Write the class Square that inherits from Rectangle:
### [11. Square size](./models/square.py)
* Update the class Square by adding the public getter and setter size
### [12. Square update](./models/square.py)
* Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:
### [13. Rectangle instance to dictionary representation](./models/rectangle.py)
* Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:
### [14. Square instance to dictionary representation](./models/square.py)
* Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:
### [15. Dictionary to JSON string](./models/base.py)
* JSON is one of the standard formats for sharing data representation.
### [16. JSON string to file](./models/base.py)
* Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:
### [17. JSON string to dictionary](./models/base.py)
* Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:
### [18. Dictionary to Instance](./models/base.py)
* Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:
### [19. File to instances](./models/base.py)
* Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:
### [21. Let's draw it](./models/base.py)
* Opens a window and draws all the Rectangles and Squares with the Turtle module:
  
---

## Author
* **MiguelCF06** - [MiguelCF06](https://github.com/MiguelCF06)
