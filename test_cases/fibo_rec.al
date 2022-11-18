// ALi
// Program to get the fibonacci series with recursion

int func fibonacci(n : int){
    
    if( n==0 ){
        return 0;
    }
    if( n==1 ){
        return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);

}

func main(){

    var n, result : int;

    void func start() {
        
        n = 10;
        result = fibonacci(n);
        print("Fibonacci of ", n, " is: ", result);

    }

    void func update() {
        // The update is not used for this test
    }
}