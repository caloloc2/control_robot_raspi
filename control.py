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

# definicion de funciones

def activa(pin, estado):
    GPIO.output(pin, estado)

def lee(pin):
    return GPIO.input(pin)

tipo = False # False:manual - True:automatico (se lee desde el GPIO 11)

try:
    while(True):
        tipo = lee(11)
        while(tipo):
            print "automatico"   
            time.sleep(0.1)
        print "."
except KeyboardInterrupt:
    print "chao"
    GPIO.cleanup()