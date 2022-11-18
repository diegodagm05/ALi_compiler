// ALi
// Program to sort an array using Bubble sort algorithm

func main(){

    // arr starts at 8000, ends at 8010
    var arr[10] : array<int>;
    // i = 8010, j = 8011, size = 8012, aux = 8013
    var i, j, size, aux : int;

    void func start() {
        
        arr = [5, 3, 9, 8, 6, 7, 2, 1, 4, 10];
        // Bubble sort algorithm
        size = 10;
        print("size = ", size) << endl;
        print("Array before bubble sort: ") << endl;
        for(i = 0; i < size - 1; i = i+1) {
            print(arr[i], " ");
        }
        print(" ") << endl;
        for( i = 0; i < size - 1; i = i+1 ){
            
            for( j = 0; j < size - i - 1; j = j+1){

                if( arr[j] < arr[j+1] ){
                    aux  = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = aux;
                }
            }
        }
        print("Array after bubble sort:") << endl;
        for(i = 0; i < size - 1; i = i+1) {
            print(arr[i], " ");
        }
        
    }

    void func update() {
        // The update is not used for this test
    }
}