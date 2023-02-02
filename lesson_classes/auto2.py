class AutoService:
    car_count = 0

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model
        self.engine_status = False
        AutoService.car_count += 1
        print(f'Автомобиль "{self.make}" покинул конвейер')

    def __str__(self):
        return f'''Информация о автомобиле:
Марка: {self.make};
Модель: {self.name};
Состояние двигателя: {self.check_engine_status()}
'''

    def check_engine_status(self):
        return 'Двигатель запущен' if self.engine_status == True else 'Двигатель выключен'

    def start(self):
        match self.engine_status:
            case bool(status) if status == False:
                self.engine_status = True
        return self.check_engine_status()

    def stop(self):
        if self.engine_status == True:
            self.engine_status = False
        return self.check_engine_status()


my_lada = AutoService('Гранта', 'Лада', 2023)
print(my_lada)
