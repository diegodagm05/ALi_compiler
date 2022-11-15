var PI : float;
var VAR : int; 

void func init_global_vars() {
    print("Initializing global vars");
    PI = 3.14;
    VAR = 78;
}

int func calculateSum(paramX : int) {
    var a : int;
    a = VAR + paramX;
    return a;
}

func main() {
    // First, declare your variables
    var a, b, c : int;
    var j, k, l: float;
    var x : char;
    // Assignment statements
    init_global_vars();
    a = VAR;
    b = VAR + 1;
    c = calculateSum(b);
    print("Calculate sum result is: ", c);
    x = 'c';
    j = 3.14;
    k = 2.71;
    l = 14.14;
    // conditional statments
    if (a != b && !(b > c)) {
        print("Hello world!");
    } elif (a >= b && j > k || j < l || a <= c) {
        print("Hello universe!");
    } else {
        read("myFile.txt");
        l = k;
    }

    void func start() {
        j = k;
    
    }

    void func update() {

    }
}