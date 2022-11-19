// This file will probably not be able to run
var PI : float;
var VAR : int; 


void func init_global_vars() {
    PI = 3.14;
    VAR = 78;
}

void func drawPlayer(xpos : int, ypos: int, xsize: int, ysize : int) {
    var isActive : bool;
    drawGameObject(xpos, ypos, xsize*2, ysize*2, "blue");
}

func main() {
    // First, declare your variables
    var height, event, width : int;
    init_global_vars();

    void func start() {
        // generating a canvas with 1080 width, 800 in height and a red background
        generateCanvas(1080, 800, "#FF0000");
        setCanvasTitle("MyGame");
    }

    void func update() {
        height = getWindowHeight();
        width = getWindowWidth();
        event = getGameEvent();
        // quit game when user presses escape key
        if (event == 5) {
            quitGame();
        }
        // setting background to blue
        setCanvasBackground("#0000FF");
        drawPlayer(20, 20+1, height, width);
    }
}