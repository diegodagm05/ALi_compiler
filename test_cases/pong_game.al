// ALi
// Program to execute a basic Pong game.

void func drawPlayer(xpos : int, ypos: int, xsize: int, ysize : int) {
    drawGameObject(xpos, ypos, xsize, ysize, "#3311BB");
}

void func drawPong(xpos : int, ypos: int, xsize: int, ysize : int) {
    drawGameObject(xpos, ypos, xsize, ysize, "#33BB44");
}

func main() {
    // First, declare your variables
    var playerXPos, startPlayerPosX, startPlayerPosY, playerSpeed, playerWidth, playerHeight: int; 
    var canvasHeight, canvasWidth, event, windowWidth, windowHeight : int;
    var pongPosX, pongPosY, pongSpeedX, pongSpeedY, pongDirectionX, pongDirectionY : int;
    var hasGameStarted : bool;
    canvasWidth = 1080;
    canvasHeight = 720;
    playerWidth = 100;
    playerHeight = 40;
    playerSpeed = 10;
    hasGameStarted = false;

    void func start() {
        generateCanvas(canvasWidth, canvasHeight, "#FCFCFC");
        setCanvasTitle("My Pong Game - Press Tab to start the game");
        windowWidth = getWindowWidth();
        windowHeight = getWindowHeight();
        startPlayerPosX = (windowWidth / 2) / 10;
        startPlayerPosY = windowHeight - playerHeight - 10;
        playerXPos = startPlayerPosX;
        pongPosX = 1;
        pongPosY = 1;
        pongSpeedX = 10;
        pongSpeedY = 10;
        pongDirectionX = 1;
        pongDirectionY = 1;
    }

    void func update() {
        event = getGameEvent();
        // quit game when user presses escape key
        if (event == 5) {
            quitGame();
        } elif (event == 1) {
            playerXPos = playerXPos - 1;
        } elif (event == 3) {
            playerXPos = playerXPos + 1;
        } elif(event == 0) {
            hasGameStarted = true;
        }
        drawPlayer(playerXPos * playerSpeed, startPlayerPosY, playerWidth, playerHeight);
        // make pong rebound
        if (hasGameStarted) {
            setCanvasTitle("My Pong Game - Game has started!");
            if (pongPosX > playerXPos && pongPosX < (playerXPos + playerWidth / 2) && (pongPosY * pongSpeedY) == startPlayerPosY) {
                // change direction to up
                pongDirectionY = -1;
            } elif((pongPosX <= 0 || pongPosX >= canvasWidth / 10) && (pongPosY * pongSpeedY) < canvasHeight) {
                // change x direction to be the opposite direction
                pongDirectionX = pongDirectionX * -1;
            } elif (pongPosY == 0) {
                // change direction to down
                pongDirectionY = 1;
                pongPosY = 1;
            } elif ((pongPosY * pongSpeedY) > canvasHeight) {
                setCanvasTitle("You lost!");
                setCanvasBackground("#DD1111");
            }
            pongPosX = pongPosX + pongDirectionX;
            pongPosY = pongPosY + pongDirectionY;
            drawPong(pongPosX * pongSpeedX, pongPosY * pongSpeedY, 20, 20);
        }
    }
}