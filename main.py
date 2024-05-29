class Vehicle:

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheels):
        if wheels == "2":
            vehicle_type = "мотоцикл"
        elif wheels == "3":
            vehicle_type = "трицикл"
        elif wheels == "4":
            vehicle_type = "автомобиль"
        else:
            return "Я не знаю таких ТС"
        return f"Это {vehicle_type} марки {self.name}"
