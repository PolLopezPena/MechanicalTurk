import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

StepPins = [24, 25, 8, 7]
StepPins2 = [17, 18, 27, 22]

for pin in StepPins:
    print("SetUp Pins1")
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
for pin in StepPins2:
    print("SetUp Pins2")
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

electroIman = 21
GPIO.setup(electroIman, GPIO.OUT)
waitTime = 0.002

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


def steps(number, pins):
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


numberStepPerRevolution = 200

def moveDiagonal(wayX, wayY ):
        stepC = 0
        stepCounterX = 0
        stepCounterY = 0
        while stepC < int(numberStepPerRevolution):
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
if __name__ == '__main__':
    GPIO.output(electroIman, GPIO.HIGH)
    hasRun = False
    while not hasRun:
            steps(numberStepPerRevolution, StepPins2)
            time.sleep(1)
            #steps(stepsPerSquare*ySteps, StepPins)
            #time.sleep(1)
            hasRun = True
    print("Stop Motos")
    for pin in StepPins:
            GPIO.output(pin, False)
    for pin in StepPins2:
            GPIO.output(pin, False)
    GPIO.output(electroIman, GPIO.LOW)
    #GPIO.output(electroIman, GPIO.HIGH)
    #moveDiagonal(1, -1)
    #GPIO.output(electroIman, GPIO.LOW)
