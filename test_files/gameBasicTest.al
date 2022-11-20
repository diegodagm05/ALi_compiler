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
    var height, event, width : int;
    init_global_vars();

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
        print("Inside update -> event = ", event, " width -> ", width, " height ->", height) << endl;
        // quit game when user presses escape key
        if (event == 5) {
            quitGame();
        } elif (event == 1) {
            setCanvasTitle("Reset canvas title");
        } else {
            print("Unrecognized game event") << endl;
        }
        // setting background to blue
        setCanvasBackground("#0000FF");
        drawPlayer(20, 20, height / 4, width / 4);
    }
}