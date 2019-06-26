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

def activa(pin):
    GPIO.output(pin, True)
    time.sleep(0.1)
    GPIO.output(pin, False)

def lee(pin):
    return GPIO.input(pin)

def learn(pos):
    if (sensors[pos]>0.2):
        sensors[pos]-=0.2

tipo = False # False:manual - True:automatico (se lee desde el GPIO 11)
sensors = [3,3,3]

try:
    while(True):
        tipo = lee(11)
        while(tipo):
            print "Modo Automatico"
            if (lee(9)): # sensor izquierdo
                time.sleep(sensors[0])
                activa(5)
                learn(0)
            tipo = lee(11)
            time.sleep(0.02)
        print "Modo Manual"
        time.sleep(0.02)
except KeyboardInterrupt:
    print "chao"
    GPIO.cleanup()