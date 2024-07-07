# This is a sample Python script.
import chess
from stockfish import  Stockfish
import time
import RPi.GPIO as GPIO
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

def init():
        GPIO.setmode(GPIO.BCM)
        magnet = 21
        StepPins = [24, 25, 8, 7]
        StepPins2 = [17, 18, 27, 22]
        for pin in StepPins2:
                print("SetUp Pins1")
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, False)
        for pin in StepPins:
                print("SetUp Pins2")
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, False)
        GPIO.setup(magnet, GPIO.OUT)
        return StepPins, StepPins2, magnet
def moveToCoordinate(movement):
        mapping = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        row = mapping[movement[0]]
        col = int(movement[1])
        return row, col
waitTime = 0.002
#Normal-step
# Define simple sequence
StepCount1 = 4
Seq1 = []
Seq1 = [i for i in range(0, StepCount1)]
Seq1[0] = [1, 0, 0, 0]
Seq1[1] = [0, 1, 0, 0]
Seq1[2] = [0, 0, 1, 0]
Seq1[3] = [0, 0, 0, 1]
# Define advanced half-step sequence
StepCount2 = 8
Seq2 = []
Seq2 = [i for i in range(0, StepCount2)]
Seq2[0] = [1, 0, 0, 0]
Seq2[1] = [1, 1, 0, 0]
Seq2[2] = [0, 1, 0, 0]
Seq2[3] = [0, 1, 1, 0]
Seq2[4] = [0, 0, 1, 0]
Seq2[5] = [0, 0, 1, 1]
Seq2[6] = [0, 0, 0, 1]
Seq2[7] = [1, 0, 0, 1]

Seq = Seq2
StepCount = StepCount2

x1 = 0
y1 = 0
x2 = 8
y2 = 8

stepsPerSquare = 2200

def steps(number, pins):
    print(pins)
    StepCounter = 0
    if number < 0:
        sign = -1
    else:
        sign = 1
    nb = abs(number)*2  # Half-step
    for i in range(nb):
        for pin in range(4):
            xpin = pins[pin]
            if Seq[StepCounter][pin] != 0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
        StepCounter += sign

        if StepCounter == StepCount:
            StepCounter = 0
        if StepCounter < 0:
            StepCounter = StepCount - 1
        time.sleep(waitTime)

def moveController(xSteps, ySteps):
        hasRun = False
        while not hasRun:
                steps(-stepsPerSquare*xSteps, StepPins2)
                time.sleep(1)
                steps(stepsPerSquare*ySteps, StepPins)
                time.sleep(1)
                hasRun = True
        print("Stop Motos")
        for pin in StepPins:
                GPIO.output(pin, False)
        for pin in StepPins2:
                GPIO.output(pin, False)

def moveDiagonal(way):
        stepC = 0
        stepCounter1 = 0
        while stepC < int(stepsPerSquare):
                for pin in range(4):
                        xpin1 = StepPins[pin]
                        if Seq[stepCounter1][pin] != 0:
                                GPIO.output(xpin1, True)
                        else:
                                GPIO.output(xpin1, False)
                        xpin2 = StepPins2[pin]
                        if Seq[stepCounter1][pin] != 0:
                                GPIO.output(xpin2, True)
                        else:
                                GPIO.output(xpin2, False)
                stepCounter1 += way
                if StepCounter1 == StepCount:
                        StepCounter = 0
                if StepCounter1 < 0:
                        StepCounter1 = StepCount - 1
                time.sleep(waitTime)
                stepC +=1
        print("Stop Motos")
        for pin in StepPins:
                GPIO.output(pin, False)
        for pin in StepPins2:
                GPIO.output(pin, False)

#Movement Pieces
def bishopMovement(wayX, wayY, xsteps, ysteps):
        stepC = 0
        stepCounterX = 0
        stepCounterY = 0
        while stepC < int(stepsPerSquare*2):
                for pin in range(4):
                        xpin1 = StepPins[pin]
                        if Seq[stepCounterY][pin] != 0:
                                GPIO.output(xpin1, True)
                        else:
                                GPIO.output(xpin1, False)
                        xpin2 = StepPins2[pin]
                        if Seq[stepCounterX][pin] != 0:
                                GPIO.output(xpin2, True)
                        else:
                                GPIO.output(xpin2, False)
                stepCounterX += wayX
                stepCounterY += wayY
                if stepCounterX == StepCount:
                        stepCounterX = 0
                if stepCounterX < 0:
                        stepCounterX = StepCount - 1
                if stepCounterY == StepCount:
                        stepCounterY = 0
                if stepCounterY < 0:
                        stepCounterY = StepCount - 1
                time.sleep(waitTime)
                stepC +=1
                
        print("Stop Motos")
        for pin in StepPins:
                GPIO.output(pin, False)
        for pin in StepPins2:
                GPIO.output(pin, False)
def horseMovement(xsteps, ysteps):
        moveDiagonal(1)
        time.sleep(2)
        moveController(xsteps, ysteps)
        time.sleep(2)
        moveDiagonal(-1)
def rookMovement(xsteps, ysteps):
        hasRun = False
        if xsteps != 0:
               steps1 = xsteps 
        else:
                steps1 = ysteps
        while not hasRun:
                steps(-stepsPerSquare*steps1, StepPins2)
                time.sleep(1)
                hasRun = True
        print("Stop Motos")
        for pin in StepPins:
                GPIO.output(pin, False)
        for pin in StepPins2:
                GPIO.output(pin, False)
def queenMovement(xsteps, ysteps):
        if xsteps == ysteps:
                if xsteps < 0:
                        wayX = -1
                else:
                        wayX = 1
                if ysteps < 0:
                        wayY = -1
                else:
                        wayY = 1
                for step in range(xsteps):
                        bishopMovement(wayX, wayY, xsteps, ysteps)
        else:
                rookMovement(xsteps, ysteps)
def pawnMovement(xsteps, ysteps):
        if xsteps == 0:
                hasRun = False
                while not hasRun:
                        steps(-stepsPerSquare*ysteps, StepPins)
                        time.sleep(1)
                        hasRun = True
                print("Stop Motos")
                for pin in StepPins:
                        GPIO.output(pin, False)
                for pin in StepPins2:
                        GPIO.output(pin, False)
        else:
                if xsteps < 0:
                        wayX = -1
                else:
                        wayX = 1
                if ysteps < 0:
                        wayY = -1
                else:
                        wayY = 1
                bishopMovement(wayX, wayY, xsteps, ysteps)
                
def movementPieces(typeM, xsteps, ysteps):
        if typeM == 'R':
                rookMovement(xsteps, ysteps)
        elif typeM == 'N':
                horseMovement(xsteps, ysteps)                
        elif typeM == 'B':
                if xsteps < 0:
                        wayX = -1
                else:
                        wayX = 1
                if ysteps < 0:
                        wayY = -1
                else:
                        wayY = 1
                for step in range(xsteps):
                        bishopMovement(wayX, wayY, xsteps, ysteps)
        elif typeM == 'Q':
                queenMovement(xsteps, ysteps)
        elif typeM == 'K':
                queenMovement(xsteps, ysteps)
        elif typeM == 'P':
                pawnMovement()
if __name__ == '__main__':
    StepPins,StepPins2, electroIman = init()
    board = chess.Board()
    time.sleep(2)
    while(board.is_checkmate() == False):
        stockfish1 = Stockfish("/home/alexquper/RLP/Robotica/Stockfish-sf_15/src/stockfish")
        stockfish1.set_depth(10)
        stockfish1.set_skill_level(10)
        move1 = input('Enter the posotion of the piece: ')
        move2 = input('Enter the position of the square: ')
        move = move1 + move2
        board.push_san(move)
        print(board)
        stockfish1.set_fen_position(board.fen())
        moveIA2 = stockfish1.get_best_move()
        piece2 = moveIA2[0] + moveIA2[1]
        square2 = moveIA2[2] + moveIA2[3]
        board.push_san(moveIA2)
        print(board)
        print(moveIA2)
        x1, y1 = moveToCoordinate(piece2)
        print(x1,y1)
        xsteps = x1 - x2
        ysteps = y1 - y2
        moveController(xsteps, ysteps)
        time.sleep(2)
        
        x2, y2 = moveToCoordinate(square2)
        xsteps = x2 - x1
        ysteps = y2 - y1
        #ActivarElectroIman
        GPIO.output(electroIman, GPIO.HIGH)
        time.sleep(2)
        typePiece = board.piece_at(chess.parse_square(square2))
        print(typePiece)
        movementPieces(typePiece, xsteps, ysteps)
        GPIO.output(electroIman, GPIO.LOW)
        print("Stop Iman")
        #ApagamosElectroIman
        time.sleep(2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
