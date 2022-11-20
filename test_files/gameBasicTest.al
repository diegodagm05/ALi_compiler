// This file will probably not be able to run
var PI : float;
var VAR : int; 


void func init_global_vars() {
    PI = 3.14;
    VAR = 78;
}

void func drawPlayer(xpos : int, ypos: int, xsize: int, ysize : int) {
    var isActive : bool;
    drawGameObject(xpos, ypos, xsize+1, ysize+1, "#00FFCC");
}

func main() {
    // First, declare your variables
    var height, event, width, xpos, ypos : int;
    init_global_vars();

    xpos = 20; 
    ypos = 20;

    void func start() {
        // generating a canvas with 1080 width, 800 in height and a red background
        // generateCanvas(500, 500, "#FF0000");
        print("Ran start function") << endl;
        setCanvasTitle("MyGame");
    }

    void func update() {
        height = getWindowHeight();
        width = getWindowWidth();
        event = getGameEvent();
        // print("Inside update -> event = ", event, " width -> ", width, " height ->", height) << endl;
        // quit game when user presses escape key
        if (event == 5) {
            quitGame();
        } elif (event == 1) {
            print("Pressed leftarrow key");
            xpos = xpos - 1;
        } elif (event == 2) {
            ypos = ypos + 1;
        } elif (event == 3) {
            xpos = xpos + 1;
        } elif (event == 4) {
            ypos = ypos - 1;
        } elif(event == 0) {
            print("Reset position") << endl;
            xpos = 20;
            ypos = 20;
        }
        // setting background to blue
        // setCanvasBackground("#0000FF");
        drawPlayer(xpos, ypos, height / 4, width / 4);
        
    }
}