func main(){
    
    var i, j : int;
    var A[8], B[4][5] : array<int>;
    var C[2][2], D[10] : array<float>;
    var k : float;
    var CH[5], CH2[10][10] : array<char>;
    var c1 : char;
    var BLS[3][3] : array<bool>;
    var b1 : bool;

    void func start() {
        A[4] = 5;
        // This should throw an error
        B[0][5] = 6; 
    }

    void func update() {
        
    }

}