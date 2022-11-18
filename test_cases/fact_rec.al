// ALi
// Program to calculate the factorial of a number with recursion.

int func factorial(n : int){
    
    if( n==0 ){
        return 1;
    }
    return n * factorial(n - 1);
}

func main(){

    var n, result : int;

    void func start() {
        
        n = 5;
        result = factorial(n);
        print("The factorial of ", n, " is: ", result);

    }

    void func update() {
        // The update is not used for this test
    }
}