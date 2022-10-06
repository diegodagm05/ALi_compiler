var PI : float;

int func foo() {
    // PI = 3.14;
    print("Hello");
    return PI;
}

float func bar(param1 : int, param2 : float) {
    var PI : float;
    PI = 3.1416;
    six_pi = 2 + PI + 6;
    return param1 * param2;
}

func main() {
    // First, declare your variables
    var a, k : int;
    var b, m : float;
    var c : char;
    var arr : array[3]; 
    // Assignment statements
    a = 20;
    j = foo(); 
    b = 23.67;
    m = bar(a, b) / foo(); 
    c = 'c';
    arr = [1,2,3];
    // conditional statments
    if (a != b) {
        print("Hello world!");
    } elif (a >= b && j > arr[1] || b < arr[3] || a <= arr[2]) {
        print("Hello universe!");
    } else {
        read("myFile.txt");
    }
    // Foor loop
    for k = 0 until k < 3 {
        print("Arr[k]() :", arr[k]);
    }
    // While loop
    while (k < 6) {
        print("Hello all!");
    }
}