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
    - [Calls to functions](#calls-to-functions)
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
    // Return type functions must return a value
    // The type of the value must match the function signature
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
ALi has thre main types of expressions: arithmetic, relational and logical. All of these can be assigned to a variable of the corresponding type.
```
func main(){
    var a, b : int;
    var x, y : float;
    var q, w : char;
    var i, j, k : bool;
    a = 3;
    b = a + 2; // This is an example of an arithmetic expression
    x = 3.14;
    y = 3.14 / 2;
    q = 'a';
    w = 'b';
    i = true;
    k = a > b; // This is an example of a relational expression 
    k = k && i; // This is an example of a logical expression
    
    void func start() {
        // this runs at the start of a game

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
    }
}
```
The full semantic cube for ALi is as follows:
|  left operator |  right operator |   +   |   -   |   *   |   /   |  &&  | \|\| |  ==  |  !=  |   >  |   <  |  >=  |  <=  |  <=  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:---:|
|  int  |  int  |  int  |  int  |  int  |  int  | bool | bool | bool | bool | bool | bool | bool | bool |  int  |
|  int  | float | float | float | float | float |  err |  err |  err |  err | bool | bool | bool | bool |  err  |
|  int  |  char |  err |  err  |  err  |  err  |  err |  err |  err |  err |  err |  err |  err |  err |  err  |
|  int  |  bool |  err  |  err  |  err  |  err  |  err |  err |  err |  err |  err |  err |  err |  err |  err  |
| float | float | float | float | float | float |  err |  err | bool | bool | bool | bool | bool | bool | float |
| float |  char |  err  |  err  |  err  |  err  | errl |  err |  err |  err |  err |  err |  err |  err |  err  |
| float |  bool |  err  |  err  |  err  |  err  |  err |  err |  err |  err |  err |  err |  err |  err |  err  |
|  char |  char |  err |  err |  err  |  err  |  err |  err | bool | bool | bool | bool | bool | bool |  char |
|  char |  bool |  err  |  err  |  err  |  err  |  err |  err |  err |  err |  err |  err |  err |  err |  err  |
|  bool |  bool |  err  |  err  |  err  |  err  | bool | bool | bool | bool |  err |  err |  err |  err |  bool |

### Calls to functions
Once we have functions declared, we should be able to call them.
```
void func bar(isPrintingFoo : bool) {
    // do something here, but do not return a value
}

int func foo() {
    return 2;
}

func main(){
    var a, b : int;
    var is_bool : bool;
    // to call a function 
    is_bool = false;
    bar(is_bool);
    // A function that returns a value should be called as part of an expression or assignment
    a = foo();
    b = foo() * a;
    void func start() {
        // this runs at the start of a game

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
    }
}
```
### Keyboard input (Game Events)
ALi only receives keyboard inputs specific to events that are listened to inside of the game loop. In reality, this is a special function, but it has its own nuance and is therefore explained separately to the rest of the game engine specific functions.

The function `getGameEvent()` returns an integer value which specifies what game event was recieved from the keyboard. The events are listened to *on keydown*, and are identified as follows. 
|          Event          | ID |
|:-----------------------:|:--:|
| Pressed Tab Key         | 0  |
| Pressed Left Arrow Key  | 1  |
| Pressed Up Arrow Key    | 2  |
| Pressed Right Arrow Key | 3  |
| Pressed Down Arrow Key  | 4  |
| Pressed Escape Key      | 5  |
| No game event received  | -1 |

We can perform game specific actions when recieving one of these events.
```
func main(){
    var event: int;
    void func start() {
        // this runs at the start of a game

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
        event = getGameEvent();
        // do something with the game event
    }
}
```
### Console output
ALi enables printing strings to the console with the usage of the `print` keyword. This is one of the lone instances (outside of the special functions) where ALi allows the usage of strings. 

We can have several different variables or string constants printed out in one same print statement by separating the varibales of strings with commas. To specify that we want a the console output to end by outputing a new line, we need to add `<< endl` to the end of our print statment. 
```
func main(){
    var event: int;
    void func start() {
        // this runs at the start of a game
        print("Hello from the start procedure! This string will not print a new line at the end... ");

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
        event = getGameEvent();
        print("Hello from the update loop! This will show up several times!") << endl;
        print("Recieved the following event identifier = ", event) << endl;
    }
}
```
### Conditionals
To handle control flow through conditional statements, ALi provides several options. We can have: 
- A simple `if` statement
- An `if` statement followed by one or more `elif` statement
- An `if` statement followed by one `else` statement
- AN `if` statement followed by one or more `elif` statements ending in one `else` statement.
```
func main(){
    var event, x, y : int;
    var is_bool : bool;
    is_bool = true;
    if (is_bool) {
        print("Its true!") << endl;
    }
    x = 0;
    y = 1;
    is_bool = x == y;
    if (is_bool) {
        print("Its still true!") << endl;
    } else {
        print("Its false now") << endl;
    }
    void func start() {
        // this runs at the start of a game
        print("Hello from the start procedure! This string will not print a new line at the end... ");

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
        event = getGameEvent();
        if (event == 0) {
            print("Pressed the tab key!") << endl;
        } elif (event == 1) {
            print("Pressed the left arrow key!") << endl;
        } elif (event == 2) {
            print("Pressed the up arrow key!") << endl;
        } else {
            print("I don't know what they pressed...") << endl;
        }
    }
}
```
### While/For Loops
For repetitive code blocks we have `while` and `for` loops. 

A `while` loop evaluates an expression and executes the following block if the expression evaluates to `true`. 
```
func main(){
    var x, y : int;
    var is_bool : bool;
    is_bool = true;
    x = 0;
    y = 10;
    while(is_bool) {
        x = x + 1;
        y = y - 1;
        if (x == y) {
            is_bool = false;
        }
    }
    void func start() {
        // this runs at the start of a game
        print("Hello from the start procedure! This string will not print a new line at the end... ");

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
    }
}
```

A `for` loop initializes a control variable, evaluates an expression, executes the following block if the expression evaluates to `true`, and finally reassigns an expression to a variable. ALi does not enforce that this reassignment occurs to the variable that was initialized at the beggining of the `for` loop. However, this reassignment also modifies this variable in a way that it cannot be modified inside the `for` loop.

```
func main(){
    var counter : int;
    for (counter = 0; counter < 10; counter = counter + 1) {
        print(counter);
        counter = 20; // This line will not increment the counter, the 20 only lives in the counter variable until the next iteration
    }
    
    void func start() {
        // this runs at the start of a game
        print("Hello from the start procedure! This string will not print a new line at the end... ");

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
    }
}
```
### Arrays
ALi enbles declaration and usage of vectors and matrices (1D arrays and 2D arrays). These arrays must be declared with fixed dimensions. To access the index of an array we can use an integer variable or an expression that evaluates to an integer value. Arrays can be initialized with a set of expression separated by commas.
```
func main(){
    var i, j, A[3], B[2][2] : array<int>;
    i = 2;
    j = i + 3;
    A = [23, i, j*2];
    B[1][0] = i;
    
    void func start() {
        // this runs at the start of a game
        print("Hello from the start procedure! This string will not print a new line at the end... ");

    }

    void func update() {
        // The update refreshes the game canvas every time it is called 
        // to enable drawing on it and listening to events
    }
}
```
### Game engine special functions
| Function | Description | Properties | Example |
| -------- | ----------- | ---------- | ------- |
| start() | Procedure that will initialize the game | It is called once, at the start of every game | N/A |
| update() | Procedure that executes the infinite game loop | It is called every frame. It updates the screen to show a new image on every frame of the game loop. | N/A |
| generateCanvas(width, height, backgroundColor) | It takes in a height and width as integer values for the dimensions of the window and a string that specifies the background color (hex) of the window. |  If this function is not called, the game window will be set by default to 720pxx720px with a black background. This function must be called on the start() function of the main procedure. If it is called it must be the first procedure called on the start() function. | generateCanvas(900,1080, "#FCFCFC"); |
| setCanvasTitle(title) | Sets the title of the game window by taking in a string constant. | Title must be a string constant | setCanvasTitle("My ALi Game"); |
| setCanvasBackground(backgroundColor) | Updates the background color for the game window. | The background color must be a string constant representing a color with hexadecimal code | setCanvasBackground("#FF1111"); |
| getWindowWidth | Returns the width of the game window. | The returned value is an integer.This function is treated the same as an expression. | windowHeight = getWindowHeight(); |
| getWindowHeight() | Returns the height of the game window. | The returned value is an integer. This function is treated the same as an expression. | windowHeight = getWindowHeight(); | 
| getGameEvent() | Returns one of the possible game events: key up, key down, pressed left arrow key, pressed right arrow key, pressed up arrow key, pressed down arrow key, pressed escape or pressed tab. The events will be obtained on keydown. | The events returned will be represented as an [enumerated list](#keyboard-input-game-events). This function is treated the same as an expression. | event = getGameEvent(); |
| drawGameObject(xpos, ypos, xsize, ysize, color) | Makes a figure of size xsize by ysize at position xpos, ypos and gives it a color determined by the color parameter. | xsize, ysize, xpos, and ypos are integers representing pixels. color is an hexadecimal string representing a color. | drawGameObject(xpos, ypos, 50, 50, "#00FF00"); |
| quitGame() |   Quits the game.We would generally like to have the user have an ESC key press to control when the game ends. | This function should be called somewhere in the infinite game loop to exit a game properly | `if (event == 5) { quitGame(); }` |

