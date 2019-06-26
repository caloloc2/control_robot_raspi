import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT) ## GPIO 5 como salida
GPIO.setup(6, GPIO.OUT) ## GPIO 6 como salida
GPIO.setup(13, GPIO.OUT) ## GPIO 13 como salida

GPIO.setup(22, GPIO.IN) ## GPIO 22 como entrada
GPIO.setup(10, GPIO.IN) ## GPIO 10 como entrada
GPIO.setup(9, GPIO.IN) ## GPIO 9 como entrada
GPIO.setup(11, GPIO.IN) ## GPIO 11 como entrada

print "Inicio programa..."

ite = 0
while ite<20:
    GPIO.output(5, True)
    GPIO.output(6, True)
    GPIO.output(13, True)
    time.sleep(0.5)
    GPIO.output(5, False)
    GPIO.output(6, False)
    GPIO.output(13, False)
    time.sleep(0.5)
    ite += 2

print "Fin programa."

GPIO.cleanup()