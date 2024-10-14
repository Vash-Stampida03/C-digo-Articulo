import ydlidar

class MyLidar:
    def __init__(self):
        ydlidar.os_init()
        self.ports = ydlidar.lidarPortList()
        self.port = "/dev/ydlidar"
        for key, value in self.ports.items():
            self.port = value
        self.laser = ydlidar.CYdLidar()
        self.laser.setlidaropt(ydlidar.LidarPropSerialPort, self.port)
        self.laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 115200)
        self.laser.setlidaropt(ydlidar.LidarPropLidarType, ydlidar.TYPE_TRIANGLE)
        self.laser.setlidaropt(ydlidar.LidarPropDeviceType, ydlidar.YDLIDAR_TYPE_SERIAL)
        self.laser.setlidaropt(ydlidar.LidarPropScanFrequency, 10.0)
        self.laser.setlidaropt(ydlidar.LidarPropSampleRate, 9)
        self.laser.setlidaropt(ydlidar.LidarPropSingleChannel, True)
        self.ret = self.laser.initialize()

    def iniciarlidar(self):
        if self.ret:
            self.ret = self.laser.turnOn()
        return self.ret

    def pararlidar(self):
        self.laser.turnOff()

    def get_dato(self):
        scan = ydlidar.LaserScan()
        if self.laser.doProcessSimple(scan):
            return scan.points
        else:
            return None