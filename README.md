# ALi
2D Video Game Engine. Final project for Tecnológico de Monterrey's Design of Compilers course.
- [ALi](#ali)
  - [Contribution](#contribution)
  - [User Manual](#user-manual)
    - [Compilation and execution](#compilation-and-execution)
    - [Basic structure of an ALi file](#basic-structure-of-an-ali-file)
    - [Declaration of variables](#declaration-of-variables)
    - [Declaration of functions](#declaration-of-functions)
    - [Expressions](#expressions)
      - [Arithmetic expressions](#arithmetic-expressions)
      - [Relational expressions](#relational-expressions)
      - [Boolean expressions](#boolean-expressions)
    - [Calls to functions](#calls-to-functions)
    - [Returning values from functions](#returning-values-from-functions)
    - [Keyboard input (Game Events)](#keyboard-input-game-events)
    - [Console output](#console-output)
    - [Conditionals](#conditionals)
    - [While/For Loops](#whilefor-loops)
    - [Arrays](#arrays)
    - [Game engine special functions](#game-engine-special-functions)

## Contribution
This project is being written in Python using PLY with a virtual environment. To create and activate this virtual environment run
```
python3 -m venv ./venv && source ./venv/bin/activate
```

To install the project dependencies run
```
pip install -r ./requirements.txt
```
## User Manual
### Compilation and execution
To install the project dependencies run
```
pip install -r ./requirements.txt
```

To compile and execute an ALi file run
```
python ali /path/to/your/file.al
```
Note that a file **must** have the `.al` extension to be compiled and executed by the ALi Game Engine.

### Basic structure of an ALi file
The most barebones version of an ALi file is as follows. 
```
// You may declare global variables here

// Followed by functions


func main(){
    // You can also declare variables inside of the main function scope

    void func start() {
        // this runs at the start of a game

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
    }
}
```
### Declaration of variables
ALi has four main datatypes that can be used to declare variables:`int`, `float`, `char`, `bool`.
```
// These are global variables
// Int variable declaration
var a, b, c : int;
// Float variable declaration
var x, y, z : float;
// Char variable declaration
var q, w, e : char;
// Boolean variable declaration
var is_boolean : bool;

func main(){
    // Int variable declaration
    var a, b, c : int;
    // Float variable declaration
    var x, y, z : float;
    // Char variable declaration
    var q, w, e : char;
    // Boolean variable declaration
    var is_boolean : bool;
    
    void func start() {
        // this runs at the start of a game

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
    }
}
```
Note that if this were to be declared, the variables inside the `main` scope hold precedence, as in ALi, local variables have precedence over global ones.
### Declaration of functions
There are two main types of functions in ALi. There are `void` functions, which do not return a value. There are return functions, which specify a retur value from the basic datatypes: `int`, `float`, `char`, `bool`. It is also possible to have any number of parameters in a function, specifying their type is required as well. 
```
int func foo(paramX : int) {
    // You can also declare variables inside of a function
    var a : int;
    a = 10 * paramX;
    // return type functions should return a value
    return a;
}

void func bar(isPrintingFoo : bool) {
    // do something here, but do not return a value
}

float func invalidFunction() {
    // Careful! This will cause an error in compilation since the return statement type does not match the function signature
    return 1;
}

func main(){
    
    
    void func start() {
        // this runs at the start of a game

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
    }
}
```
### Expressions
#### Arithmetic expressions
#### Relational expressions
#### Boolean expressions
### Calls to functions
### Returning values from functions
### Keyboard input (Game Events)
### Console output
### Conditionals
### While/For Loops
### Arrays
### Game engine special functions