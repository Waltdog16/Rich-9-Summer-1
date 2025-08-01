########## 1.3 ##########
import pgzrun
import random
GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
GUARDMOVEINTERVAL = 0.2
PlAYER_MOVE_INTERVAL =0.1
BACKGROUND_SEED = 12345
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
#########################
########## 1.5 ##########
MAP = ["WWWWWWWWWWWWWWWW",
       "WWK           GW",
       "WWWWWWWW  WWWWWW",
       "W              W",
       "W              W",
       "W            WGW",
       "W            WWW",
       "W   P          W",
       "W              W",
       "W       WWWWWW W",
       "W      WG    K W",
       "WWWWWWWWWWWWWDWW"]
#########################
########## 1.4 ##########
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
def DrawBackground():
    random.seed(BACKGROUND_SEED)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y))
            if x % 2 == y % 2:
                screen.blit("floor2", GetScreenCoords(x,y))
            else:
                screen.blit("floor1", GetScreenCoords(x,y))
            n = random.randint(0,99)
            if n < 5:
                screen.blit("crack1", GetScreenCoords(x,y))
            elif n < 10:
                screen.blit("crack2", GetScreenCoords(x,y))
#########################
########## 2.1 ##########
def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
#########################
########## 1.7, 3.0, 3.3 ##########
def SetupGame():
    global player
    global keysToCollect
    global gameOver
    global guards
    global playerWon
    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []
    guards = []
    gameOver = False
    playerWon = False
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = GetScreenCoords(x, y)
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"))
                guard.pos = GetScreenCoords(x, y)
                guards.append(guard)
#########################
########## 1.6 ##########
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))
#########################
########## 1.8, 3.1 ##########
def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()
#########################
############# 3.5 ##############
def drawGameOver():
    screenMiddle = (WIDTH / 2, HEIGHT / 2)
    screen.draw.text("GAME OVER", midbottom=screenMiddle,
                     fontsize=GRID_SIZE, color="indigo", owidth=1)
    if playerWon:
        screen.draw.text("VICTORY ACHIEVED!", midtop=screenMiddle,
                     fontsize=GRID_SIZE, color="blue", owidth=1)
    else:
        screen.draw.text("YOU LOSE BUCKO", midtop=screenMiddle,
                     fontsize=GRID_SIZE, color="orange", owidth=1)
    screen.draw.text("Press Space to try again", midtop=(WIDTH/2, HEIGHT/2 + GRID_SIZE),
                     fontsize=GRID_SIZE/2, color="red", owidth=1)
#########################
############# 4.1 ##################
def MoveGuard(guard):
    global gameOver
    if gameOver:
        return
    (playerX, playerY) = GetActorGridPos(player)
    (guardX, guardY) = GetActorGridPos(guard)
    if playerX > guardX and MAP[guardY][guardX + 1] != "W":
        guardX += 1
    elif playerX < guardX and MAP[guardY][guardX - 1] != "W":
        guardX -= 1
    elif playerY > guardY and MAP[guardY + 1][guardX] != "W":
        guardY += 1
    elif playerY < guardY and MAP[guardY - 1][guardX] != "W":
        guardY -= 1
    animate(guard, pos=GetScreenCoords(guardX,guardY),
            duration=GUARDMOVEINTERVAL)
    if guardX == playerX and guardY == playerY:
        gameOver = True
#########################
########## 4.2 ##########
def MoveAllGuards():
    for guard in guards:
        MoveGuard(guard)
#########################
########## draw() ##########
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        drawGameOver()
#########################
def on_key_up(key):
    if key == key.SPACE and gameOver:
        SetupGame()
########## 2.2, 3.2 ##########
def MovePlayer(dx, dy):
    global gameOver
    global playerWon
    if gameOver:
        return
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == "W":
        return
    elif square == "D":
        if len(keysToCollect) > 0:
            return
        else:
            gameOver = True
            playerWon = True
    for key in keysToCollect:
        (keyX, keyY) = GetActorGridPos(key)
        if x == keyX and y == keyY:
            keysToCollect.remove(key)
            break
    animate(player, pos=GetScreenCoords(x,y),
                duration=PlAYER_MOVE_INTERVAL)
#########################
########## 2.3 ##########
def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.DOWN:
        MovePlayer(0, 1)
#########################
# Start the game
SetupGame()
clock.schedule_interval(MoveAllGuards, GUARDMOVEINTERVAL)
pgzrun.go()

















