import MotorLib

class Motores:
    def __init__(self):
        self.motor_right_front = MotorLib.Motor(11, 12)
        self.motor_left_back = MotorLib.Motor(23, 18)
        self.motor_left_front = MotorLib.Motor(15, 13)
        self.motor_right_back = MotorLib.Motor(21, 19)

    def stop(self):
        self.motor_right_front.stop_Motor()
        self.motor_left_back.stop_Motor()
        self.motor_left_front.stop_Motor()
        self.motor_right_back.stop_Motor()

    def adelante(self, speed=100):
        self.motor_right_front.forward_Motor(speed)
        self.motor_left_back.forward_Motor(speed)
        self.motor_left_front.forward_Motor(speed)
        self.motor_right_back.forward_Motor(speed)

    def atras(self, speed=100):
        self.motor_right_front.backward_Motor(speed)
        self.motor_left_back.backward_Motor(speed)
        self.motor_left_front.backward_Motor(speed)
        self.motor_right_back.backward_Motor(speed)

    def izquierda(self, speed=100):
        self.motor_right_front.forward_Motor(speed)
        self.motor_left_back.backward_Motor(speed)
        self.motor_left_front.backward_Motor(speed)
        self.motor_right_back.forward_Motor(speed)

    def derecha(self, speed=100):
        self.motor_right_front.backward_Motor(speed)
        self.motor_left_back.forward_Motor(speed)
        self.motor_left_front.forward_Motor(speed)
        self.motor_right_back.backward_Motor(speed)

    def superiorIzquierda (self):
        self.motor_right_front.forward_Motor(100)
        self.motor_left_back.forward_Motor(20)
        self.motor_left_front.forward_Motor(20)
        self.motor_right_back.forward_Motor(100)

    def inferiorIzquierda (self):
        self.motor_right_front.backward_Motor(100)
        self.motor_left_back.backward_Motor(20)
        self.motor_left_front.backward_Motor(20)
        self.motor_right_back.backward_Motor(100)

    def superiorDerecha (self):
        self.motor_right_front.forward_Motor(20)
        self.motor_left_back.forward_Motor(100)
        self.motor_left_front.forward_Motor(100)
        self.motor_right_back.forward_Motor(20)

    def inferiorDerecha (self):
        self.motor_right_front.backward_Motor(20)
        self.motor_left_back.backward_Motor(100)
        self.motor_left_front.backward_Motor(100)
        self.motor_right_back.backward_Motor(20)