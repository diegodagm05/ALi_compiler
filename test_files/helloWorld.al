var PI : float;

int func foo() {
    PI = 3.14;
    return PI;
}

float func bar(param1 : int, param2 : float) {
    var PI_2, random_op : float;
    PI_2 = 3.1416;
    random_op = 2 + PI_2 + 6 * (7 / 3) / 3;
    return param1 * param2 + random_op;
}

void func drawPlayer(xpos : int, ypos: int, xsize: int, ysize : int) {
    var isActive : bool;
    drawGameObject(xpos, ypos, xsize*2, ysize*2, "blue");
}

func main() {
    // First, declare your variables
    var a, b, c, height, event : int;
    var j, k, l : float;
    var x : char;
    // Assignment statements
    a = 20;
    b = 10;
    c = 20 + 10;
    x = 'c';
    j = 3.14;
    k = 2.71;
    l = 14.14;
    // conditional statments
    if (a != b && !(b > c)) {
        print("Hello world!");
    } elif (a >= b && j > k || j < l|| a <= c) {
        print("Hello universe!");
    } else {
        read("myFile.txt");
        l = k;
    }
    // Foor loop
    for (a = 0; a < 3; a = a + 1) {
        print("Arr[a]() :", arr[a]);
    }
    // While loop
    while (a < 6) {
        print("Hello all!");
    }

    void func start() {
        generateCanvas(720, 720, "red");
        setCanvasTitle("MyGame");
        drawGameObject(a, k, arr[0], arr[1], "blue");
    }

    void func update() {
        drawPlayer(20, 20+1, j, k);
    }
}