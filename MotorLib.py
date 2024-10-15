import RPi.GPIO as GPIO



# Set up GPIO mode

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)



class Motor:

    def __init__(self, pin1, pin2):

        """Initialize a motor with two pins"""

        self.pin1 = pin1

        self.pin2 = pin2



        GPIO.setup(self.pin1, GPIO.OUT)

        GPIO.setup(self.pin2, GPIO.OUT)

        self.a = GPIO.PWM(self.pin1, 100)  # Configure for 100 Hz

        self.b = GPIO.PWM(self.pin2, 100)

        self.a.start(0)

        self.b.start(0)



    def stop_Motor(self):

        """Stop the motor"""

        self.a.ChangeDutyCycle(0)

        self.b.ChangeDutyCycle(0)



    def backward_Motor(self, duty_cycle):

        """Move the motor backward with a specified duty cycle"""

        self.a.ChangeDutyCycle(0)

        self.b.ChangeDutyCycle(duty_cycle)



    def forward_Motor(self, duty_cycle):

        """Move the motor forward with a specified duty cycle"""

        self.a.ChangeDutyCycle(duty_cycle)

        self.b.ChangeDutyCycle(0)