// ALi
// Program to sort an array using Bubble sort algorithm

func main(){

    var arr[10] : array<int>;
    var i, j, size, to_find: int;

    void func start() {
        
        arr[] = [5, 3, 9, 8, 6, 7, 2, 1, 4, 10];
        size = 10;
        to_find = 7;

        for( i = 0; i < size; i = i+1 ){
            if( arr[i] == to_find ){
                print("Element found at position: ", i);
            }
            elif( i > size ){
                print("Element not found in array");
            }
        }
        
    }

    void func update() {
        // The update is not used for this test
    }
}