// ALi
// Program to get the fibonacci series with loop.

int func fibonacci(n : int){
    
    var i, current, next, aux : int;
    current = 0;
    next = 1;

    for(i = 0; i <= n; i = i + 1 ){
        aux = current;
        current = next;
        next = next + aux;
    }
    return aux;

}

func main(){

    var n, result : int;

    void func start() {
        
        n = 20;
        result = fibonacci(n);
        print("Fibonacci of ", n, " is: ", result);
        quitGame();

    }

    void func update() {
        // The update is not used for this test
    }
}