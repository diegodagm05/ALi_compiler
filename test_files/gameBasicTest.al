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
    var height, event, width, xpos, ypos, speed : int;
    init_global_vars();

    xpos = 20; 
    ypos = 20;
    speed = 10;

    print("Before start function");

    void func start() {
        // generating a canvas with 1080 width, 800 in height and a red background
        // generateCanvas(500, 500, "#FF0000");
        print("Ran start function");
        setCanvasTitle("MyGame");
    }

    void func update() {
        height = getWindowHeight();
        width = getWindowWidth();
        event = getGameEvent();
        // print("Inside update -> event = ", event, " width -> ", width, " height ->", height);
        // quit game when user presses escape key
        if (event == 5) {
            quitGame();
        } elif (event == 1) {
            print("Pressed leftarrow key") << endl;
            xpos = xpos - 1;
        } elif (event == 2) {
            print("Pressed up key") << endl;
            ypos = ypos - 1;
        } elif (event == 3) {
            print("Pressed rightarrow key") << endl;
            xpos = xpos + 1;
        } elif (event == 4) {
            print("Pressed down key") << endl;
            ypos = ypos + 1;
        } elif(event == 0) {
            print("Reset position") << endl;
            xpos = 20;
            ypos = 20;
        }
        // setting background to blue
        // setCanvasBackground("#0000FF");
        drawPlayer(xpos*speed, ypos*speed, height / 4, width / 4);
        
    }
}