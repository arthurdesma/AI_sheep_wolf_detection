import RPi.GPIO as GPIO
import time

def delay_microsecondsUP(cycleMid, pin):
    start_time = time.time()
    while (time.time() - start_time) < (cycleMid):
        GPIO.output(pin, GPIO.HIGH)

def delay_microsecondsDOWN(cycleMid, pin):
    start_time = time.time()
    while (time.time() - start_time) < (cycleMid):
        GPIO.output(pin, GPIO.LOW)

gpio_pin = 18

GPIO.setmode(GPIO.BCM) # Mode de numerotation choisi ( ici pin XX choisi == num dans GPIOXX )
GPIO.setup(gpio_pin, GPIO.OUT) # On assigne la pin selectionnee a la pin correspondante de la raspbery

# Parametres du signal carre
f = 40000  # Frequence en Hz
cycle = 0.5  # Rapport cyclique (50% pour un signal carre equilibre)
T= 1.0/f   # Periode en s

tempo= (T * cycle) - 0.0000025 # une demi periode

# Generation du signal carre
try:
    while True:
        delay_microsecondsUP(tempo, gpio_pin)
        delay_microsecondsDOWN(tempo, gpio_pin)

except KeyboardInterrupt:
    GPIO.cleanup()