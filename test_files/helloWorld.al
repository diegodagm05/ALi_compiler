var PI : float = 3.1416

int func foo() {
    return 3;
}

float func bar(param1 : int, param2 : float) {
    return param1 * param2 * PI;
}

void func main() {
    var a, k : int;
    var b, m : float;
    var c : char;
    var arr : array[3]; 
    a = 20;
    j = foo(); 
    b = 23.67;
    m = bar(a, b) / foo(); 
    c = 'c';
    arr = [1,2,3];
    if (a != b) {
        print("Hello world!");
    } else if (a >= b && j > arr[1] || b < arr[3] || a <= arr[2]) {
        print("Hello universe!");
    } else {
        read("myFile.txt");
    }
}