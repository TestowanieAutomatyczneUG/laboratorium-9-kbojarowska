from unittest.mock import *
from unittest import TestCase, main

class Car:
    def needsFuel(self):
        pass
    def getEngineTemperature(self):
        pass
    def driveTo(self, destination):
        pass

class test_Car_needs_fuel(TestCase):
    def test_needs_fuel(self):
        car = Car()
        car.needsFuel = Mock(name='needs_fuel')
        car.needsFuel.return_value = True
        self.assertEqual(car.needsFuel(), True, 'return value from needsFuel incorrect')

    def test_get_engine_temperature(self):
        car = Car()
        car.getEngineTemperature = Mock(name='get_engine_temperature')
        car.getEngineTemperature.return_value = 95
        self.assertEqual(car.getEngineTemperature(), 95, 'return value from getEngineTemperature incorrect')

    def test_drive_to(self):
            car = Car()
            car.driveTo = Mock(name='drive_to')
            car.driveTo.return_value = "destination marked"
            self.assertEqual(car.driveTo("Poland"), "destination marked", 'return value from driveTo incorrect')

if __name__ == '__main__':
    main()