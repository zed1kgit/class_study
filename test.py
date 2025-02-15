import main

vehicle_1 = main.Vehicle("BMW", 20000)
vehicle_2 = main.Vehicle("Toyota", 75000)
vehicle_3 = main.Vehicle("Ford", 130000)
vehicle_4 = main.Vehicle("Honda", 200000)

print(vehicle_1.get_vehicle_type(2))
print(vehicle_1.get_vehicle_advice())
input()
print(vehicle_2.get_vehicle_type(3))
print(vehicle_2.get_vehicle_advice())
input()
print(vehicle_3.get_vehicle_type(4))
print(vehicle_3.get_vehicle_advice())
input()
print(vehicle_4.get_vehicle_type(5))
print(vehicle_4.get_vehicle_advice())
input()

monitor = main.Monitor("Samsung", "LS24C430GAIXCI", 1920, 1080, 100, "IPS")

print(monitor.get_data("matrix"))
print(monitor.get_data("state"))
input()
print(monitor.turn_on())
print(monitor.get_data("state"))
input()
print(monitor.get_aspect_ratio())