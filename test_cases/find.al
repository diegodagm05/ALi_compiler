// ALi
// Program to find an element of an array

func main(){

    var arr[10] : array<int>;
    var i, j, size, to_find: int;
    var is_in_array : bool;

    void func start() {
        
        arr = [5, 3, 9, 8, 6, 7, 2, 1, 4, 10];
        size = 10;
        to_find = 17;
        is_in_array = false;

        for( i = 0; i < size; i = i+1 ){
            if( arr[i] == to_find ){
                print("Element found at position: ", i);
                is_in_array = true;
            }
        }
        if (!is_in_array) {
            print("Element not found in array ");
        }
        quitGame();
    }

    void func update() {
        // The update is not used for this test
    }
}