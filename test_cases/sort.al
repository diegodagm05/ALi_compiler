// ALi
// Program to sort an array

func main(){

    var arr[10] : array<int>;
    var i, j, size, aux : int;

    void func start() {
        
        // Bubble sort algorithm
        size = 10;
        for( i = 0; i < size - 1; i = i+1 ){
            
            for( j = 0; j < size - i - 1; j = j+1){

                if( arr[j] < arr[j+1] ){
                    aux  = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = aux;
                }
            }
        }
        
    }

    void func update() {
        // The update is not used for this test
    }
}