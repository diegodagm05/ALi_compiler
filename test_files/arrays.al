func main(){
    
    var i, j : int;
    var A[8], B[2][2] : array<int>;
    // var C[2][2], D[10] : array<float>;
    // var k : float;
    // var CH[5], CH2[10][10] : array<char>;
    // var c1 : char;
    // var BLS[3][3] : array<bool>;
    var b1 : bool;

    A = [1, 2, 3, 4, 5, 6, 7, 8];
    B = [ [0, 1], [ 2, 3 ] ];

    void func start() {
        // A[4] = 5;
        i = A[7] + 6;
        print("A[4] = i = ", i);
        // This should throw an error.
        // B[0][5] = 6; 
        B[0][1] = 13;
    }

    void func update() {
        
    }

}