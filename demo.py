
from Vehicle import vehicle as myV

krystal_car = myV.Vehicle("Krystal", "blue", 4,4,4, "Honda")
anna_car = myV.Vehicle("Anna", "red", 4,4,4, "Toyota")
ian_car = myV.Vehicle("Ian", "yellow", 4,2,2, "Nissan")
barrow_car = myV.Vehicle("Barrow", "blue", 4,4,4, "Honda")

anna_car.displayColor()
anna_car.displayWheels()
anna_car.displaySeats()
anna_car.displayWindows()
anna_car.displayBrand()
krystal_car.displayColor()
krystal_car.displayWheels()
krystal_car.displaySeats()
krystal_car.displayWindows()
krystal_car.displayBrand()
ian_car.displayColor()
ian_car.displayWheels()
ian_car.displaySeats()
ian_car.displayWindows()
ian_car.displayBrand()
barrow_car.displayColor()
barrow_car.displayWheels()
barrow_car.displaySeats()
barrow_car.displayWindows()
barrow_car.displayBrand()

krystal_car.moveBackward(10)
krystal_car.myPosition()
krystal_car.moveForward(20)
krystal_car.turnLeft()
krystal_car.moveForward(10)
krystal_car.myPosition()
krystal_car.turnRight()
krystal_car.moveBackward(20)
krystal_car.myPosition()