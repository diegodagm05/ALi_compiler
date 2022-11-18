void func foo() {
    print("Called foo!");
}

func main(){
    var i, k : int;
    var a, b : float;
    b = 1.5;
    a = b - b;
    foo();
    if (a < 0) {
        print("Hello");
    } else {
        print("PRINT");
    }
    print("Left for loop");
    for (k = 0; k < 5; k = k + 1) {
        print("Inside for loop");
        i = k;
        print("i = ", i);
        print("k = ", k);
    }

    while (a < b) {
       a = a + 0.1;
       print("Inside while");
       print(a);
    }

    void func start() {
        b = a;
    }

    void func update() {
        
    }
}