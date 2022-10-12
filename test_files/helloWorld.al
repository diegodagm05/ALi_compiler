var PI : float;

int func foo() {
    // PI = 3.14;
    print("Hello");
    return PI;
}

float func bar(param1 : int, param2 : float) {
    var PI : float;
    PI = 3.1416;
    random_op = 2 + PI + 6 * (7 / 3) / 3;
    return param1 * param2 + random_op;
}

void func drawPlayer(xpos : int, ypos: int, xsize: int, ysize : int) {
    drawGameObject(xpos, ypos, xsize*2, ysize*2, "blue");
}

func main() {
    // First, declare your variables
    var a, k, width, height, event : int;
    var b, m : float;
    var c : char;
    var arr : array<int>[3]; 
    // Assignment statements
    a = 20;
    j = foo(); 
    b = 23.67;
    m = bar(a, b) / foo(); 
    c = 'c';
    arr = [1,2,3];
    // conditional statments
    if (a != b && !(b == m)) {
        print("Hello world!");
    } elif (a >= b && j > arr[1] || b < arr[3] || a <= arr[2]) {
        print("Hello universe!");
    } else {
        read("myFile.txt");
    }
    // Foor loop
    for (k = 0; k < 3; k = k + 1) {
        print("Arr[k]() :", arr[k]);
    }
    // While loop
    while (k < 6) {
        print("Hello all!");
    }

    void func start() {
        generateCanvas(720, 720, "red");
        setCanvasTitle("MyGame");
        drawGameObject(a, k, arr[0], arr[1], "blue");
    }

    void func update() {
        if (getWindowHeight() > 500) {
            height = getWindowHeight();
            event = getGameEvent();
            width = getWindowWidth() / 2;
        }
        drawPlayer(20, 20+1, k, height);
    }
}