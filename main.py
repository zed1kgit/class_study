class Vehicle:

    def __init__(self, name, mileage: int):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheels: int):
        if wheels == 2:
            vehicle_type = "мотоцикл"
        elif wheels == 3:
            vehicle_type = "трицикл"
        elif wheels == 4:
            vehicle_type = "автомобиль"
        else:
            return "Я не знаю таких ТС"
        return f"Это {vehicle_type} марки {self.name}"

    def get_vehicle_advice(self):
        if self.mileage <= 50000:
            return f"Неплохо {self.name} можно брать."
        elif self.mileage <= 100000:
            return f"{self.name} надо внимательно проверить."
        elif self.mileage <= 150000:
            return f"{self.name} надо провести полную диагностику."
        else:
            return f"{self.name} лучше не покупать."


class Monitor:

    def __init__(self, brand, model, x: int, y: int, frequency, matrix):
        self.brand = brand
        self.model = model
        self.x = x
        self.y = y
        self.frequency = frequency
        self.matrix = matrix

    def get_data(self, name_of_data):
        if name_of_data == "brand":
            return self.brand
        elif name_of_data == "model":
            return self.model
        elif name_of_data == "x":
            return self.x
        elif name_of_data == "y":
            return self.y
        elif name_of_data == "frequency":
            return self.frequency
        elif name_of_data == "matrix":
            return self.matrix
        else:
            return None
