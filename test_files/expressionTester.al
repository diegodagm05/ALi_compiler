func main() {
    // First, declare your variables
    var a, b, c : int;
    var j, k, l: float;
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