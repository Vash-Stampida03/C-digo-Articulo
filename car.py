import curses
import time
import sys
import ydlidar
import RPi.GPIO as GPIO
from motor import Motores
from lidar import MyLidar

class Car:
    def __init__(self):
        self.lidar = MyLidar()
        self.controlMotor = Motores()
        self.obstaculo = False
        self.obstaculo_trasero = False
        self.button_delay = 0.2
        self.stdscr = curses.initscr()
        curses.cbreak()
        self.stdscr.keypad(1)
        self.stdscr.nodelay(1)

    def get_obstaculo(self):
        return self.obstaculo

    def set_obstaculo(self, value):
        self.obstaculo = value

    def get_obstaculo_trasero(self):
        return self.obstaculo_trasero

    def set_obstaculo_trasero(self, value):
        self.obstaculo_trasero = value

    def controlCarrito(self):
        try:
            char = self.stdscr.getch()
        except:
            char = -1

        if char != -1:
            if char == curses.KEY_UP:
                self.controlMotor.adelante()
                time.sleep(self.button_delay)

            elif char == curses.KEY_DOWN:
                self.controlMotor.atras()
                time.sleep(self.button_delay)

            elif char == curses.KEY_LEFT:
                self.controlMotor.izquierda()
                time.sleep(self.button_delay)

            elif char == curses.KEY_RIGHT:
                self.controlMotor.derecha()
                time.sleep(self.button_delay)

            elif char == ord('p'):
                self.controlMotor.stop()
                time.sleep(self.button_delay)

            elif char == ord('q'):
                self.controlMotor.superiorIzquierda()
                time.sleep(self.button_delay)

            elif char == ord('c'):
                self.controlMotor.inferiorIzquierda()
                time.sleep(self.button_delay)

            elif char == ord('e'):
                self.controlMotor.superiorDerecha()
                time.sleep(self.button_delay)

            elif char == ord('z'):
                self.controlMotor.inferiorDerecha()
                time.sleep(self.button_delay)

            elif char == ord('x'):
                # Salir del programa
                self.lidar.pararlidar()
                curses.endwin()
                GPIO.cleanup()
                sys.exit()

    def run(self):
        if self.lidar.iniciarlidar():
            while ydlidar.os_isOk():
                dato = self.lidar.get_dato()

                if dato:
                    self.set_obstaculo(False)
                    self.set_obstaculo_trasero(False)

                    for point in dato:
                        angle = point.angle * 180 / 3.1416
                        distance = point.range
                        if 178 <= angle <= 180 and 0 < distance < 0.20:
                            self.set_obstaculo(True)
                            break
                        elif 0 <= angle <= 2 and 0 < distance < 0.20:
                            self.set_obstaculo_trasero(True)
                            break

                    if self.get_obstaculo():
                        print("Obstáculo detectado en la parte delantera, retrocediendo...")
                        self.controlMotor.stop()
                        time.sleep(0.5)
                        self.controlMotor.atras()
                        time.sleep(1)
                        self.controlMotor.stop()

                    elif self.get_obstaculo_trasero():
                        print("Obstáculo detectado en la parte trasera, avanzando...")
                        self.controlMotor.stop()
                        time.sleep(0.5)
                        self.controlMotor.adelante()
                        time.sleep(1)
                        self.controlMotor.stop()

                self.controlCarrito()
                time.sleep(0.05)

        self.lidar.pararlidar()

car = Car()
car.run()
