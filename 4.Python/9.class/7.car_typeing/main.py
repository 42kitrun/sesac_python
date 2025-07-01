from driver import Driver
from car import Car

driver = Driver('Bob', 40, '1종 보통')

driver.drive(30)

car = Car('Tesla', 'model s')

driver.assign_car(car)

driver.drive(50)
driver.drive(100)

car.update_odometer(100)
car.update_odometer(200)
car.read_odometer()