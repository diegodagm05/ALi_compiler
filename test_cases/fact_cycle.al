// ALi
// Program for recursive factorial

int func factorial(n : int){
    
    var num : int;
    num = 1;

    while( n >= 1 ){
        num = num * n;
        n = n - 1;
    }
    return num;

}

func main(){

    var n, result : int;

    void func start() {
        
        n = 5;
        result = factorial(n);
        print("The factorial of ", n, "is: ", result);

    }

    void func update() {
        // The update is not used for this test
    }
}